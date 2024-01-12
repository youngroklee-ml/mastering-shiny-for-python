from shiny import App, ui, render
import numpy as np
from matplotlib import pyplot as plt

app_ui = ui.page_fluid(
    ui.panel_title("Central limit theorem"),
    ui.row(
        ui.column(4,
            ui.input_numeric("m", "Number of samples:", 2, min=1, max=100),
        ),
        ui.column(8,
            ui.output_plot("hist"),
        ),
    ),
)

def server(input, output, session):
    @render.plot
    def hist():
        means = [np.mean(np.random.uniform(size=input.m())) for _ in range(10000)]

        fig, ax = plt.subplots()
        ax.hist(means, bins=20)
        return fig

app = App(app_ui, server)
