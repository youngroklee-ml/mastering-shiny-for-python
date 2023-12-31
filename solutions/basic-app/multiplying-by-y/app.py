from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("x", label="If x is", min=1, max=50, value=30),
    ui.input_slider("y", label="and y is", min=1, max=50, value=5),
    "then, x times y is",
    ui.output_text("product"),
)

def server(input, output, session):
    @output
    @render.text
    def product():
        return input.x() * input.y()

app = App(app_ui, server)
