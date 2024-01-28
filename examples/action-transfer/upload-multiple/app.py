from shiny import App, ui, render
import pandas as pd

app_ui = ui.page_fluid(
    ui.input_file("upload", None, button_label="Upload...", multiple=True),
    ui.output_table("files"),
)

def server(input, output, session):
    @render.table
    def files():
        return pd.DataFrame(input.upload())

app = App(app_ui, server)
