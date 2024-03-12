from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.input_numeric("min", "Minimum", 0),
    ui.input_numeric("max", "Maximum", 3),
    ui.input_slider("n", "n", min=0, max=3, value=1),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.min)
    def _():
        ui.update_slider("n", min=input.min())
    
    @reactive.effect
    @reactive.event(input.max)
    def _():
        ui.update_slider("n", max=input.max())

app = App(app_ui, server)
