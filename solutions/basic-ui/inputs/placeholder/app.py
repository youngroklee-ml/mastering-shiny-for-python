from shiny import App, ui

app_ui = ui.page_fluid(
    ui.input_text("name", None, placeholder="Your name"),
)

def server(input, output, session):
    ...

app = App(app_ui, server)
