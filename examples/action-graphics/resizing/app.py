from shiny import App, ui, render, reactive
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
from matplotlib import pyplot as plt

np.random.seed(1014)
df = pd.DataFrame({
    'x': np.random.normal(size=100),
    'y': np.random.normal(size=100)
})

def compute_distance(df, position, xvar, yvar):
    points = df[[xvar, yvar]].copy().to_numpy()
    click = np.array([[position['x'], position['y']]])

    # Compute distance
    dist = pairwise_distances(points, click)

    return dist

app_ui = ui.page_fluid(
    ui.output_plot("plot", click=True),
)

def server(input, output, session):
    dist = reactive.value([1 for _ in range(df.shape[0])])

    @reactive.effect
    @reactive.event(input.plot_click)
    def _():
        dist.set(compute_distance(df, input.plot_click(), xvar='x', yvar='y'))
    
    @render.plot
    def plot():
        size = np.minimum(np.power(dist.get(), 5), 300)
        res = plt.scatter(df['x'], df['y'], s=size)
        return res

app = App(app_ui, server)
