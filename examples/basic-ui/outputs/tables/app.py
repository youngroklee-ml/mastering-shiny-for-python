from shiny import App, ui, render
from pydataset import data

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    ui.output_table("static"),
    ui.output_data_frame("dynamic"),
)

def server(input, output, session):
    @output
    @render.table
    def static():
        return mtcars
    
    @output
    @render.data_frame
    def dynamic():
        return render.DataTable(mtcars, filters=True, height='240px')

app = App(app_ui, server)
