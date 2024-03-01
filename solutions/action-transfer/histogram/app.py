from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

app_ui = ui.page_fluid(
    ui.input_file("file", "Upload CSV", accept=".csv"),
    ui.input_select("var", "Variable", choices=[None]),
    ui.output_plot("histogram"),
    ui.row(
        ui.column(4,
                  ui.input_select("ext", "Download file type",
                                  choices=['png', 'pdf', 'svg'],
                                  selected='png')),    
        ui.column(6, ui.download_button("download_hist", "Download histogram")),
    ),
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
    
    @reactive.calc
    def hist_plot():
        req(input.var())
        fig = plt.figure()
        plt.hist(data()[input.var()])
        return fig

    @render.plot
    def histogram():
        return hist_plot()
    
    @session.download(filename=lambda: f"histogram.{input.ext()}")
    def download_hist():
        with io.BytesIO() as buf:
            hist_plot().savefig(buf, format=input.ext())
            yield buf.getvalue()



app = App(app_ui, server)
