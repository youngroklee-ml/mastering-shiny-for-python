from shiny import App, ui, reactive, render
from pydataset import data
from plotnine import ggplot, aes, geom_histogram, geom_freqpoly, geom_density

diamonds = data("diamonds")

app_ui = ui.page_fluid(
    ui.input_select("geom", "geom function",
        choices=["geom_histogram", "geom_freqpoly", "geom_density"]
    ),
    ui.navset_hidden(
        ui.nav_panel("param1",
            ui.input_numeric("binwidth", "binwidth", value=0.1, step=0.1),
        ),
        ui.nav_panel("param2",
            ui.input_select("bw", "bw", 
                choices=["nrd0", "normal_reference", "scott", "silverman"],
                selected="nrd0"
            ),
        ),
        id="params",
    ),
    ui.output_plot("plot"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.geom)
    def _():
        match input.geom():
            case "geom_histogram":
                panel = "param1"
            case "geom_freqpoly":
                panel = "param1"
            case "geom_density":
                panel = "param2"

        ui.update_navs("params", selected=panel)

    @render.plot
    def plot():
        plot = ggplot(diamonds, aes('carat'))
        if input.geom() == "geom_histogram":
            res = plot + geom_histogram(binwidth=input.binwidth())
        elif input.geom() == "geom_freqpoly":
            res = plot + geom_freqpoly(binwidth=input.binwidth())
        elif input.geom() == "geom_density":
            res = plot + geom_density(bw=input.bw())

        return res

app = App(app_ui, server)
