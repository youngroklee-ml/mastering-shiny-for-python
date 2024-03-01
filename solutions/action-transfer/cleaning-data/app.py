from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import pandas as pd
import janitor
import os

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
    
    # Clean ------------------------------------
    @reactive.calc
    def tidied_snake():
        out = raw()
        if input.snake():
            out = out.clean_names(case_type='snake')
        return out
    
    @reactive.calc
    def tidied_empty():
        out = tidied_snake()
        if input.empty():
            out.dropna(how='all', axis=1, inplace=True)
        return out
    
    @reactive.calc
    def tidied_constant():
        out = tidied_empty()
        if input.constant():
            out = out.drop_constant_columns()
        return out

    @render.table
    def preview2():
        return tidied_constant().head(input.rows())
    
    # Download --------------------------------
    @session.download(filename=lambda: f"{os.path.splitext(input.file()[0]['name'])[0]}.tsv")
    def download():
        yield tidied_constant().to_csv(None, sep="\t", index=False)


app = App(app_ui, server)
