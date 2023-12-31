from shiny import App, ui
from pydataset import data

app_ui = ui.page_fluid(
    ui.input_select("dataset", label="Dataset", choices=list(data()['dataset_id'])),
    ui.output_text_verbatim("summary"),
    ui.output_table("table")
)

def server(input, output, session):
    ...

app = App(app_ui, server)
