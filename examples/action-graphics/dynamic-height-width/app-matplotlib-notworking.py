from shiny import App, ui, render, reactive
import matplotlib.pyplot as plt
from numpy.random import normal

app_ui = ui.page_fluid(
    ui.input_slider("height", "height", min=100, max=500, value=250),
    ui.input_slider("width", "width", min=100, max=500, value=250),
    ui.output_plot("plot"),
)

def server(input, output, session):
    @render.plot
    def plot():
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(input.width()*px, input.height()*px))
        res = ax.scatter(normal(size=20), normal(size=20))
        return res

app = App(app_ui, server)
