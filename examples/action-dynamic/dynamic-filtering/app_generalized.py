from shiny import App, ui, reactive, render
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype
from pydataset import data
import janitor
from functools import reduce

dfs = data()['dataset_id'].to_list()

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

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("_dataset", label="Dataset", choices=dfs),
            ui.output_ui("_filter"),
        ),
        ui.output_table("_data"),
    )
)

def server(input, output, session):
    @reactive.calc
    def cleaned_data():
        return data(input._dataset()).clean_names(case_type='snake')

    @reactive.calc
    def _vars():
        return cleaned_data().columns
    
    @render.ui
    def _filter():
        return list(map(lambda x: make_ui(cleaned_data()[x], x), _vars())),

    @reactive.calc
    def selected():
        each_var = map(lambda x: filter_var(cleaned_data()[x], input[x]()), _vars())
        res = reduce(lambda x, y: x & y, each_var)
        
        return res
    
    @render.table
    def _data():
        return cleaned_data()[selected()].head(12)

app = App(app_ui, server)
