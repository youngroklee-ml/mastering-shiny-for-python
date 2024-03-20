from shiny import App, ui, reactive, render
import numpy as np
import matplotlib.pyplot as plt

parameter_tabs = ui.navset_hidden(
    ui.nav_panel("normal",
                 ui.input_numeric("mean", "mean", value=1),
                 ui.input_numeric("sd", "standard deviation", min=0, value=1),
    ),
    ui.nav_panel("uniform",
                 ui.input_numeric("min", "min", value=0),
                 ui.input_numeric("max", "max", value=1),
    ),
    ui.nav_panel("exponential",
                 ui.input_numeric("rate", "rate", value=1, min=0)
    ),
    id="params"
)

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("dist", "Distribution", 
                            choices=["normal", "uniform", "exponential"]
            ),
            ui.input_numeric("n", "Number of samples", value=100),
            parameter_tabs,
        ),
        ui.output_plot("hist"),
    )
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.dist)
    def _():
        ui.update_navs("params", selected=input.dist())
    
    @reactive.calc
    def sample():
        match input.dist():
            case "normal":
                res = np.random.normal(input.mean(), input.sd(), input.n())
            case "uniform":
                res = np.random.uniform(input.min(), input.max(), input.n())
            case "exponential":
                res = np.random.exponential(1 / input.rate(), input.n())
            case _:
                res = None
        
        return res
    
    @render.plot
    def hist():
        plt.hist(sample())

app = App(app_ui, server)
