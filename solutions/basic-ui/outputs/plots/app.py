from shiny import App, ui, render
from matplotlib import pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.output_plot("plot", width="700px", height="300px")
)

def server(input, output, session):
    @output
    @render.plot(alt="A scatterplot of five random numbers")
    def plot():
        return plt.scatter(np.random.uniform(size=5), np.random.uniform(size=5))
    
app = App(app_ui, server)
