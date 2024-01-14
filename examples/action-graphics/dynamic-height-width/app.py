from shiny import App, ui, render, reactive
import matplotlib.pyplot as plt
from numpy.random import normal

app_ui = ui.page_fluid(
    ui.input_slider("height", "height", min=100, max=500, value=250),
    ui.input_slider("width", "width", min=100, max=500, value=250),
    ui.output_ui("plot_container"),
)

def server(input, output, session):
    @render.plot
    def plot():
        return plt.scatter(normal(size=20), normal(size=20))

    @render.ui
    def plot_container():
        return ui.output_plot("plot", 
                              height=f"{input.height()}px", 
                              width=f"{input.width()}px")

app = App(app_ui, server)
