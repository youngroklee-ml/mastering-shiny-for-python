from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from asyncio import sleep

app_ui = ui.page_fluid(
    ui.input_action_button("goodnight", "Good night"),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.effect
    @reactive.event(input.goodnight)
    async def _():
        ui.notification_show("So long")
        await sleep(1)
        ui.notification_show("Farewell", type="message")
        await sleep(1)
        ui.notification_show("Auf Wiedersehen", type="warning")
        await sleep(1)
        ui.notification_show("Adieu", type="error")

app = App(app_ui, server)
