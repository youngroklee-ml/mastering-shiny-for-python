from shiny import App, ui, render, reactive
import random

app_ui = ui.page_fluid(
    ui.input_text("name", "What's your name?"),
    ui.output_text("greeting"),
)

def server1(input, output, session):
    @render.text
    def greeting():
        return f"Hello {input.name()}"

def server2(input, output, session):
    @reactive.calc
    def string():
        return f"Hello {input.name()}"
    
    @render.text
    def greeting():
        return string()

def server3(input, output, session):
    @render.text
    def greeting():
        return f"Hello {input.name()}"

server = random.sample([server1, server2, server3], k=1)[0]

app = App(app_ui, server)

