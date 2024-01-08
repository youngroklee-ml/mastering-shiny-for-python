from shiny import App, ui, render, reactive
import sys

app_ui = ui.page_fluid(
    ui.input_slider("x", "x", value=1, min=0, max=10),
    ui.input_slider("y", "y", value=2, min=0, max=10),
    ui.input_slider("z", "z", value=3, min=0, max=10),
    ui.output_text("total"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.x)
    def _():
        print(f"Updating y from {input.y()} to {input.x() * 2}", file=sys.stderr)
        ui.update_slider("y", value=input.x()*2, session=session)
    
    @reactive.calc
    def total():
        total = input.x() + input.y() + input.z()
        sys.stderr.write(f"New total is {total}\n")
        return total
    
    @output(id="total")
    @render.text
    def print_total():
        return total()
    
app = App(app_ui, server)

