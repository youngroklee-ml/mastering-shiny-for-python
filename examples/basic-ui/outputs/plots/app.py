from shiny import App, ui, render
from matplotlib import pyplot as plt

app_ui = ui.page_fluid(
    ui.output_plot("plot", width="400px")
)

def server(input, output, session):
    @output
    @render.plot
    def plot():
        return plt.scatter([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

app = App(app_ui, server)
