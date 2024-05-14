from shiny import App, ui, reactive, render
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype, is_datetime64_dtype
import janitor
from functools import reduce
from datetime import datetime

data = pd.DataFrame({
    'date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03']).to_pydatetime(),
    'datetime': pd.to_datetime(['2021-01-01 00:00:00', '2021-01-02 01:00:00', '2021-01-03 23:59:59'])
})

def make_ui(x, var):
    if is_numeric_dtype(x):
        rng = (x.min(), x.max())
        res = ui.input_slider(var, var, min=rng[0], max=rng[1], value=rng)
    elif is_string_dtype(x):
        levs = list(np.unique(x))
        res = ui.input_select(var, var, choices=levs, selected=levs, multiple=True)
    elif is_datetime64_dtype(x):
        rng = (x.min().to_pydatetime().date(), x.max().to_pydatetime().date())
        res = ui.input_date_range(var, var, min=rng[0], max=rng[1], start=rng[0], end=rng[1])
    else:
        res = None

    return res

def filter_var(x, val):
    if is_numeric_dtype(x):
        res = (~np.isnan(x)) & (x >= val[0]) & (x <= val[1])
    elif is_string_dtype(x):
        res = np.isin(x, val)
    elif is_datetime64_dtype(x):
        res = (~np.isnan(x)) & \
            (x >= datetime.combine(val[0], datetime.min.time())) & \
            (x <= datetime.combine(val[1], datetime.max.time()))
    else:
        res = True
    
    return res

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.output_ui("_filter"),
        ),
        ui.output_table("_data"),
    )
)

def server(input, output, session):
    @render.ui
    def _filter():
        return list(map(lambda x: make_ui(data[x], x), data.columns))

    @reactive.calc
    def selected():
        each_var = map(lambda x: filter_var(data[x], input[x]()), data.columns)
        res = reduce(lambda x, y: x & y, each_var)
        
        return res
    
    @render.table
    def _data():
        return data[selected()].head(12)

app = App(app_ui, server)
