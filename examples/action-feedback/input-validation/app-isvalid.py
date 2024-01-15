from shiny import App, ui, render, reactive, req
from shiny_validate import InputValidator

app_ui = ui.page_fluid(
    ui.input_numeric("n", "n", value=10),
    ui.output_text("half"),
)

def server(input, output, session):
    iv = InputValidator()

    iv.add_rule("n", lambda x: "Please select an even number" if x%2 != 0 else None)
    iv.enable()

    @render.text
    def half():
        req(iv.is_valid())
        return input.n()/2

app = App(app_ui, server)
