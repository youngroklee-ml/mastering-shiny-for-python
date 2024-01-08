from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from pydataset import data
from matplotlib import pyplot as plt

cars = data('cars')

def f(x):
    return g(x)

def g(x):
    return h(x)

def h(x):
    return x**2

app_ui = ui.page_fluid(
    ui.input_select("n", "N", list(range(1, 11))),
    ui.output_plot("plot"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.plot
    def plot():
        n = f(int(input.n()))
        return plt.scatter(cars[:n]['speed'], cars[:n]['dist'])

app = App(app_ui, server)
