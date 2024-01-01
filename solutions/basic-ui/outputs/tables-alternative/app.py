from shiny import App, ui, render
from shinywidgets import output_widget, render_widget
from ipydatagrid import DataGrid
from pydataset import data

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    output_widget("dynamic"),
)

def server(input, output, session):
    @output
    @render_widget
    def dynamic():
        return DataGrid(mtcars, selection_model='row')

app = App(app_ui, server)
