from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_text("name", "What's your name?", value=None),
    ui.output_text("greeting"),
)

def server(input, output, session):
    @output
    @render.text
    def greeting():
        return f"Hello {input.name()}"

app = App(app_ui, server)
