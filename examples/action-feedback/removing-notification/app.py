from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from shiny.types import FileInfo
import pandas as pd

app_ui = ui.page_fluid(
    ui.input_file("file", "Add CSV file", accept=".csv"),
    ui.output_table("table")
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def data():
        id = ui.notification_show("Reading data...",
            duration=None, close_button=False)
        
        file: list[FileInfo] | None = input.file()
        if file is None:
            res = pd.DataFrame()
        else:
            res = pd.read_csv(file[0]["datapath"])

        ui.notification_remove(id)
        
        return res
        
    @render.table
    def table():
        return data().head()


app = App(app_ui, server)
