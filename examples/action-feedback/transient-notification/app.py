from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from time import sleep

app_ui = ui.page_fluid(
    ui.input_action_button("goodnight", "Good night"),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.effect
    @reactive.event(input.goodnight)
    def _():
        ui.notification_show("So long")
        sleep(1)        
        ui.notification_show("Farewell", type="message")
        sleep(1)        
        ui.notification_show("Auf Wiedersehen", type="warning")
        sleep(1)        
        ui.notification_show("Adieu", type="error")

app = App(app_ui, server)
