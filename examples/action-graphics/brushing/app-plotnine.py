from shiny import App, render, ui, req
from plotnine import ggplot, aes, geom_point
from pydataset import data

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    ui.output_plot("plot", brush=True),
    ui.output_text_verbatim("info"),
)

def server(input, output, session):
    @render.plot
    def plot():
        res = (ggplot(mtcars, aes('wt', 'mpg'))
               + geom_point())
        return res
    
    @render.text
    def info():
        req(input.plot_brush())
        return input.plot_brush()

app = App(app_ui, server)
