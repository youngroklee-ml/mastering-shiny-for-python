from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.input_numeric("n", "Simulations", 10),
    ui.input_action_button("simulate", "Simulate"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.n)
    def _():
        label = f"Simulate {input.n()} times"
        ui.update_action_button("simulate", label=label)

app = App(app_ui, server)
