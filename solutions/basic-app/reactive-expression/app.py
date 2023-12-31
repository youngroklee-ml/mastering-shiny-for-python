from shiny import App, ui, render, reactive

app_ui = ui.page_fluid(
    ui.input_slider("x", label="If x is", min=1, max=50, value=30),
    ui.input_slider("y", label="and y is", min=1, max=50, value=5),
    "then, (x * y) is", ui.output_text("product"),
    "and, (x * y) + 5 is", ui.output_text("product_plus5"),
    "and (x * y) + 10 is", ui.output_text("product_plus10"),
)

def server(input, output, session):
    @reactive.calc
    def x_times_y():
        return input.x() * input.y()

    @output
    @render.text
    def product():
        return x_times_y()
    
    @output
    @render.text
    def product_plus5():
        return x_times_y() + 5
    
    @output
    @render.text
    def product_plus10():
        return x_times_y() + 10

app = App(app_ui, server)
