from shiny import App, render, ui, req
from matplotlib import pyplot as plt
from pydataset import data

mtcars = data("mtcars")

# brushed_points(mtcars, {'xmin': 2, 'xmax': 3, 'ymin': 20, 'ymax': 30}, 'wt', 'mpg')
def brushed_points(df, position, xvar, yvar):
    in_region = ((df[xvar] > position['xmin']) 
                 & (df[xvar] < position['xmax'])
                 & (df[yvar] > position['ymin'])
                 & (df[yvar] < position['ymax']))
    
    return df[in_region]


app_ui = ui.page_fluid(
    ui.output_plot("plot", brush=True),
    ui.output_table("data"),
)

def server(input, output, session):
    @render.plot
    def plot():
        res = plt.scatter(mtcars['wt'], mtcars['mpg'])
        return res
    
    @render.table
    def data():
        req(input.plot_brush())
        return brushed_points(mtcars, input.plot_brush(), xvar='wt', yvar='mpg')

app = App(app_ui, server)
