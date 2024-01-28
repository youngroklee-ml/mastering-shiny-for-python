from shiny import App, ui, render, reactive, req
import pandas as pd
from pydataset import data

datasets = list(data()["dataset_id"])

app_ui = ui.page_fluid(
    ui.input_select("dataset", "Pick a dataset", datasets),
    ui.output_table("preview"),
    ui.download_button("download_tsv", "Download .tsv"),
)

def server(input, output, session):
    @reactive.calc
    def df():
        return data(input.dataset())
    
    @render.table
    def preview():
        req(isinstance(df(), pd.DataFrame))
        return df().head()
    
    @session.download(filename='test.tsv')
    def download_tsv():
        yield df().to_csv(None, sep="\t", index=False)


app = App(app_ui, server)