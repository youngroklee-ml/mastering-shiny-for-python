from shiny import App, ui, render, reactive
from time import sleep
import random

app_ui = ui.page_fluid(
    ui.input_numeric("steps", "How many steps?", 10),
    ui.input_action_button("go", "go"),
    ui.output_text("result"),
)

def server(input, output, session):
    @reactive.calc
    @reactive.event(input.go)
    def data():
        with ui.Progress() as p:
            p.set(message="Computing random number")
            for i in range(1, input.steps()):
                p.inc(1/input.steps())
                sleep(0.5)
        
        return random.uniform(0, 1)
    
    @render.text
    def result():
        return round(data(), 2)

app = App(app_ui, server)
