from shiny import App, ui, render
import shinyswatch
from plotnine import ggplot, aes, geom_point, geom_smooth
from pydataset import data

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    shinyswatch.theme.darkly(),
    ui.panel_title("A themed plot"),
    ui.output_plot("plot"),
)

def server(input, output, session):
    @render.plot
    def plot():
        res = (ggplot(mtcars, aes(x='wt', y='mpg'))
                + geom_point()
                + geom_smooth(method='lm'))
        
        return res

app = App(app_ui, server)
