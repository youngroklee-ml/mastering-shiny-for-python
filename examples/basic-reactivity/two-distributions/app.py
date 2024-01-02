from shiny import App, ui, render, reactive
import pandas as pd
from plotnine import ggplot, geom_freqpoly, aes, coord_cartesian
from scipy.stats import ttest_ind
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

def t_test(x1, x2):
    test = ttest_ind(x1, x2)
    return f"p value: {test.pvalue:.3f}\n[{test.confidence_interval().low:.2f}, {test.confidence_interval().high:.2f}]"

app_ui = ui.page_fluid(
    ui.row(
        ui.column(4,
            "Distribution 1",
            ui.input_numeric("n1", label="n", value=1000, min=1),
            ui.input_numeric("mean1", label="µ", value=0, step=0.1),
            ui.input_numeric("sd1", label="σ", value=0.5, min=0.1, step=0.1),
        ),
         ui.column(4,
            "Distribution 2",
            ui.input_numeric("n2", label="n", value=1000, min=1),
            ui.input_numeric("mean2", label="µ", value=0, step=0.1),
            ui.input_numeric("sd2", label="σ", value=0.5, min=0.1, step=0.1),
        ),
        ui.column(4,
            "Frequency polygon",
            ui.input_numeric("binwidth", label="Bin Width", value=0.1, step=0.1),
            ui.input_slider("range", label="range", value=(-3, 3), min=-5, max=5),
        ),
    ),
    ui.row(
        ui.column(9, ui.output_plot("hist")),
        ui.column(3, ui.output_text_verbatim("ttest"))
    ),
)

def server(input, output, session):
    @reactive.calc
    def x1():
        return np.random.normal(input.mean1(), input.sd1(), size=input.n1())
    
    @reactive.calc
    def x2():
        return np.random.normal(input.mean2(), input.sd2(), size=input.n2())

    @render.plot
    def hist():
        return freqpoly(x1(), x2(), binwidth=input.binwidth(), xlim=input.range())
    
    @render.text
    def ttest():
        return t_test(x1(), x2())

app = App(app_ui, server)
