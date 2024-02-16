from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import pandas as pd

ui_upload = ui.layout_sidebar(
    ui.sidebar(
        ui.input_file("file", "Data", button_label="Upload..."),
        ui.input_text("delim", "Delimiter (leave blank to guess)", ""),
        ui.input_numeric("skip", "Rows to skip", 0, min=0),
        ui.input_numeric("rows", "Rows to preview", 10, min=1),
    ),
    ui.h3("Raw data"),
    ui.output_table("preview1"),
)

ui_clean = ui.layout_sidebar(
    ui.sidebar(
        ui.input_checkbox("snake", "Rename columns to snake case?"),
        ui.input_checkbox("constant", "Remove constant columns?"),
        ui.input_checkbox("empty", "Remove empty cols?"),
    ),
    ui.h3("Cleaner data"),
    ui.output_table("preview2"),
)

ui_download = ui.row(
    ui.column(12, ui.download_button("download", "Download cleaner data", class_="btn-block")),
)

app_ui = ui.page_fluid(
    ui_upload,
    ui_clean,
    ui_download,
)


def server(input: Inputs, output: Outputs, session: Session):
    # Upload ----------------------------------
    @reactive.calc
    def raw():
        req(input.file())
        delim = None if input.delim() == "" else input.delim()
        res = pd.read_csv(
            input.file()[0]["datapath"], 
            delimiter=delim,
            skiprows=input.skip())
        return res
    
    @render.table
    def preview1():
        return raw().head(input.rows())



app = App(app_ui, server)
