from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("x", label="If x is", min=1, max=50, value=30),
    "then x times 5 is",
    ui.output_text("product"),
)

def server(input, output, session):
    @output
    @render.text
    def product():
        return input.x() * 5

app = App(app_ui, server)
