from shiny import App, render, ui, req
from matplotlib import pyplot as plt
from pydataset import data

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    ui.output_plot("plot", click=True),
    ui.output_text_verbatim("info"),
)

def server(input, output, session):
    @render.plot
    def plot():
        res = plt.scatter(mtcars['wt'], mtcars['mpg'])
        return res
    
    @render.text
    def info():
        req(input.plot_click())
        x = round(input.plot_click()['x'], 2)
        y = round(input.plot_click()['y'], 2)
        return f"[{x}, {y}]"

app = App(app_ui, server)
