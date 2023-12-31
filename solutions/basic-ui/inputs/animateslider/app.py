from shiny import App, ui

app_ui = ui.page_fluid(
    ui.input_slider("ani", None, min=0, max=100, value=0,
                    step=5, animate=True, ticks=True),
)

def server(input, output, session):
    ...

app = App(app_ui, server)
