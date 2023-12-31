from shiny import App, ui, render
from pydataset import data

app_ui = ui.page_fluid(
    ui.input_select("dataset", label="Dataset", choices=list(data()['dataset_id'])),
    ui.output_text_verbatim("summary"),
    ui.output_table("table")
)

def server(input, output, session):
    @output
    @render.text
    def summary():
        dataset = data(input.dataset())
        return dataset.describe()
    
    @output
    @render.table
    def table():
        dataset = data(input.dataset())
        return dataset

app = App(app_ui, server)
