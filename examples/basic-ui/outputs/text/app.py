from shiny import App, ui, render
import pandas as pd

app_ui = ui.page_fluid(
    ui.output_text("text"),
    ui.output_text_verbatim("code"),
)

def server(input, output, session):
    @output
    @render.text
    def text():
        return "Hello friend!"
    
    @output
    @render.text
    def code():
        x = pd.Series(range(1, 11))
        return x.describe()

app = App(app_ui, server)
