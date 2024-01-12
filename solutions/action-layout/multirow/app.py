from shiny import App, ui, render, reactive
import numpy as np
from matplotlib import pyplot as plt

app_ui = ui.page_fluid(
    ui.panel_title("Central limit theorem"),
    ui.row(
        ui.column(6, 
            ui.output_plot("hist"),
        ),
        ui.column(6,
            ui.output_plot("freqploy"),
        ),
    ),
    ui.row(
        ui.input_numeric("m", "Number of samples:", 2, min=1, max=100),
    ),
)

def server(input, output, session):
    @reactive.calc
    def means():
        return [np.mean(np.random.uniform(size=input.m())) for _ in range(10000)]

    @render.plot
    def hist():
        fig, ax = plt.subplots()
        ax.hist(means(), bins=20)
        return fig
    
    @render.plot
    def freqploy():
        counts, bins = np.histogram(means(), bins=20)
        return plt.plot(bins[:-1], counts)
    
app = App(app_ui, server)
