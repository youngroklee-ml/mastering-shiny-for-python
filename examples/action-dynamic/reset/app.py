from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.input_slider("x1", "x1", min=-10, max=10, value=0),
    ui.input_slider("x2", "x2", min=-10, max=10, value=0),
    ui.input_slider("x3", "x3", min=-10, max=10, value=0),
    ui.input_action_button("reset", "Reset"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.reset)
    def _():
        ui.update_slider("x1", value=0)
        ui.update_slider("x2", value=0)
        ui.update_slider("x3", value=0)

app = App(app_ui, server)
