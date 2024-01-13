from shiny import App, render, ui, req
from matplotlib import pyplot as plt
from pydataset import data
import numpy as np
from sklearn.metrics import pairwise_distances

mtcars = data("mtcars")

# near_points(mtcars, {'x': 3.5, 'y': 15}, 'wt', 'mpg')
def near_points(df, position, xvar, yvar, threshold=20):
    points = df[[xvar, yvar]].copy().to_numpy()
    click = np.array([[position['x'], position['y']]])

    # Convert data into pixel scale
    # For now, put some logic
    # TO DO: revise with correct formula
    min_xvar = min([position['domain']['left'], position['domain']['right']])
    max_xvar = max([position['domain']['left'], position['domain']['right']])
    min_yvar = min([position['domain']['bottom'], position['domain']['top']])
    max_yvar = max([position['domain']['bottom'], position['domain']['top']])

    range_x = position['range']['right'] - position['range']['left']
    range_y = position['range']['top'] - position['range']['bottom']

    points[:,0] = position['range']['left'] + (points[:,0] - min_xvar) / (max_xvar - min_xvar) * range_x
    click[:,0] = position['range']['left'] + (click[:,0] - min_xvar) / (max_xvar - min_xvar) * range_x
    points[:,1] = position['range']['bottom'] + (points[:,1] - min_yvar) / (max_yvar - min_yvar) * range_y
    click[:,1] = position['range']['bottom'] + (click[:,1] - min_yvar) / (max_yvar - min_yvar) * range_y
    
    # Find points within threshold
    near = pairwise_distances(points, click) < threshold
    return df[near]


app_ui = ui.page_fluid(
    ui.output_plot("plot", click=True),
    ui.output_table("data"),
)

def server(input, output, session):
    @render.plot
    def plot():
        res = plt.scatter(mtcars['wt'], mtcars['mpg'])
        return res
    
    @render.table
    def data():
        req(input.plot_click())
        return near_points(mtcars, input.plot_click(), xvar='wt', yvar='mpg')

app = App(app_ui, server)
