from shiny import App, ui, render, reactive, req
import os
import pandas as pd

app_ui = ui.page_fluid(
    ui.input_file("file", None, accept=[".csv", ".tsv"]),
    ui.input_numeric("n", "Rows", value=5, min=1, step=1),
    ui.output_ui("out_container"),
)

def server(input, output, session):
    @reactive.calc
    def data():
        req(input.file())

        _, ext = os.path.splitext(input.file()[0]["name"])

        match ext:
            case ".csv":
                return pd.read_csv(input.file()[0]["datapath"])
            case ".tsv":
                return pd.read_csv(input.file()[0]["datapath"], delimiter="\t")
            case _:
                return None
    
    @render.ui
    def out_container():
        if isinstance(data(), pd.DataFrame):
            return ui.output_table("head")
        else:
            return ui.markdown("**Invalid file; Please upload a .csv or .tsv file**")
        
    @render.table
    def head():
        req(isinstance(data(), pd.DataFrame))
        return data().head(input.n())
                
app = App(app_ui, server)
