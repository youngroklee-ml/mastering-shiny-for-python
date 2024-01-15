from shiny import App, ui, render, reactive, req
from shiny_validate import InputValidator, check
from pydataset import data
import numpy as np

datasets = set(data()['dataset_id'])

app_ui = ui.page_fluid(
    ui.input_text("dataset", "Dataset name"),
    ui.output_table("table"),
)

def server(input, output, session):
    iv = InputValidator()
    iv.add_rule("dataset", 
                check.compose_rules(
                    check.required("Empty dataset name"),
                    check.in_set(datasets, "Unknown dataset")),
                )
                
    iv.enable()

    @reactive.calc
    def load():
        req(input.dataset())
        req(iv.is_valid(), cancel_output=True)
        return data(input.dataset())
    
    @render.table
    def table():
        return load().head()

app = App(app_ui, server)
