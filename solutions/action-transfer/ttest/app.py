from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp

app_ui = ui.page_fluid(
    ui.input_file("file", "Upload CSV", accept=".csv"),
    ui.input_select("var", "Variable", choices=[None]),
    ui.output_text_verbatim("ttest"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def data():
        req(input.file())
        res = pd.read_csv(input.file()[0]["datapath"])

        return res.select_dtypes(include=[np.number])
    
    @reactive.effect
    @reactive.event(data)
    def _():
        ui.update_select("var", choices=data().columns.tolist())
    
    @render.text
    def ttest():
        req(input.var())
        return ttest_1samp(data()[input.var()], 0)


app = App(app_ui, server)
