from shiny import App, ui, reactive, render
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype
from pydataset import data

def make_ui(x, var):
    if is_numeric_dtype(x):
        rng = (x.min(), x.max())
        res = ui.input_slider(var, var, min=rng[0], max=rng[1], value=rng)
    elif is_string_dtype(x):
        levs = list(np.unique(x))
        res = ui.input_select(var, var, choices=levs, selected=levs, multiple=True)
    else:
        res = None

    return res

def filter_var(x, val):
    if is_numeric_dtype(x):
        res = (~np.isnan(x)) & (x >= val[0]) & (x <= val[1])
    elif is_string_dtype(x):
        res = np.isin(x, val)
    else:
        res = True
    
    return res

iris = data('iris')

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            make_ui(iris['Sepal.Length'], "Sepal_Length"),
            make_ui(iris['Sepal.Width'], "Sepal_Width"),
            make_ui(iris['Species'], "Species"),
        ),
        ui.output_table("data"),
    )
)

def server(input, output, session):
    @reactive.calc
    def selected():
        res = filter_var(iris['Sepal.Length'], input['Sepal_Length']()) & \
            filter_var(iris['Sepal.Width'], input['Sepal_Width']()) &\
            filter_var(iris['Species'], input['Species']())
        
        return res
    
    @render.table
    def data():
        return iris[selected()].head(12)

app = App(app_ui, server)
