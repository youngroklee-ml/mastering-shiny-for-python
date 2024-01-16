from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from pydataset import data
from time import sleep

mtcars = data('mtcars')

app_ui = ui.page_fluid(
    ui.output_table("table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    def notify(msg, id=None):
        return ui.notification_show(msg, id=id, duration=None, close_button=False)

    @reactive.calc
    def data():
        id = notify("Reading data...")
        sleep(1)

        notify("Reticulating splines...", id=id)
        sleep(1)

        notify("Herding llamas...", id=id)
        sleep(1)

        notify("Orthogonalizing matrices...", id=id)
        sleep(1)

        ui.notification_remove(id)
        return mtcars

    @render.table
    def table():
        return data().head()


app = App(app_ui, server)
