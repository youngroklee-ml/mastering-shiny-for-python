from shiny import App, ui, reactive
import datetime

app_ui = ui.page_fluid(
    ui.input_numeric("year", "year", value=2020),
    ui.input_date("date", "date", value=datetime.date(2020, 1, 1)),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.year)
    def _():
        d = datetime.date(
            input.year(),
            input.date().month,
            28 if input.date().month == 2 and input.date().day == 29 else input.date().day
        )
        ui.update_date("date", 
                       value=d,
                       min=datetime.date(input.year(), 1, 1),
                       max=datetime.date(input.year(), 12, 31))

app = App(app_ui, server)
