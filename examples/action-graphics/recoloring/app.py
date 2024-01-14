from shiny import App, render, ui, reactive
from matplotlib import pyplot as plt
from pydataset import data
import pandas as pd

mtcars = data("mtcars")

# brushed_points(mtcars, {'xmin': 2, 'xmax': 3, 'ymin': 20, 'ymax': 30}, 'wt', 'mpg')
def brushed_points(df, position, xvar, yvar):
    in_region = ((df[xvar] > position['xmin']) 
                 & (df[xvar] < position['xmax'])
                 & (df[yvar] > position['ymin'])
                 & (df[yvar] < position['ymax']))
    
    return df[in_region], in_region


app_ui = ui.page_fluid(
    ui.output_plot("plot", brush=True, dblclick=True),
)

def server(input, output, session):
    selected = reactive.value([False for _ in range(mtcars.shape[0])])

    @reactive.effect
    @reactive.event(input.plot_brush)
    def _():
        _, brushed = brushed_points(mtcars, input.plot_brush(), xvar='wt', yvar='mpg')
        selected.set(brushed | selected.get())
    
    @reactive.effect
    @reactive.event(input.plot_dblclick)
    def _():
        selected.set([False for _ in range(mtcars.shape[0])])

    @render.plot
    def plot():
        color = pd.Categorical(selected(), categories=[True, False])
        fig, ax = plt.subplots()
        res = ax.scatter(mtcars['wt'], mtcars['mpg'], c=color, label=color)
        # produce a legend with the unique colors from the scatter
        legend1 = ax.legend(*res.legend_elements(), loc="lower left", title="Classes")
        ax.add_artist(legend1)        
        return res

app = App(app_ui, server)
