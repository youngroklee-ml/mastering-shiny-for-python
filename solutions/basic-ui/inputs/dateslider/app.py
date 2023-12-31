from shiny import App, ui
import datetime

app_ui = ui.page_fluid(
    ui.input_slider("date", "When should we deliver?",
                    min=datetime.date(2020, 9, 16),
                    max=datetime.date(2020, 9, 23),
                    value=datetime.date(2020, 9, 17)),
)

def server(input, output, session):
    ...

app = App(app_ui, server)

