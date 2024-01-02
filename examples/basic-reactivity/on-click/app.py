from shiny import App, ui, render, reactive
import pandas as pd
from plotnine import ggplot, geom_freqpoly, aes, coord_cartesian
import numpy as np

def freqpoly(x1, x2, binwidth=0.1, xlim=(-3, 3)):
    df = pd.DataFrame({
        "x": np.concatenate([x1, x2]),
        "g": ["x1"] * len(x1) + ["x2"] * len(x2)
    })

    res = (ggplot(df, aes("x", colour="g"))
           + geom_freqpoly(binwidth=binwidth, size=1)
           + coord_cartesian(xlim=xlim))
    
    return res

app_ui = ui.page_fluid(
    ui.row(
        ui.column(3,
            ui.input_numeric("lambda1", "lambda1", value=3),
            ui.input_numeric("lambda2", "lambda2", value=5),
            ui.input_numeric("n", "n", value=int(1e4), min=0),
            ui.input_action_button("simulate", "Simulate!"),
        ),
        ui.column(9, ui.output_plot("hist")),
    ),
)

def server(input, output, session):
    @reactive.calc
    @reactive.event(input.simulate, ignore_none=False)
    def x1():
        return np.random.poisson(input.lambda1(), size=input.n())
    
    @reactive.calc
    @reactive.event(input.simulate, ignore_none=False)
    def x2():
        return np.random.poisson(input.lambda2(), size=input.n())
    
    @render.plot
    def hist():
        return freqpoly(x1(), x2(), binwidth=1, xlim=(0, 40))
    
app = App(app_ui, server)
