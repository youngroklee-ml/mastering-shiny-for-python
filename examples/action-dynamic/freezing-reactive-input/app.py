from shiny import App, ui, reactive, render, req
from pydataset import data

app_ui = ui.page_fluid(
    ui.input_select("dataset", "Choose a dataset", choices=("pressure", "cars")),
    ui.input_select("column", "Choose column", choices=tuple()),
    ui.output_text_verbatim("summary"),
)

def server(input, output, session):
    @reactive.calc
    def dataset():
        return data(input.dataset())
    
    @reactive.effect
    @reactive.event(input.dataset)
    def _():
        reactive.value.freeze(input.column)
        ui.update_select("column", choices=dataset().columns.tolist())
    
    @render.text
    def summary():
        return dataset()[input.column()].describe()

app = App(app_ui, server)
