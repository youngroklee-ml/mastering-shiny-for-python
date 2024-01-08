from shiny import App, ui, render, reactive
import logging

# configure logging
logging.basicConfig(format='%(message)s')
log = logging.getLogger('shiny.debugging')
log.setLevel('INFO')

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
        log.info(f"Updating y from {input.y()} to {input.x() * 2}")
        ui.update_slider("y", value=input.x()*2, session=session)
    
    @reactive.calc
    def total():
        total = input.x() + input.y() + input.z()
        log.info(f"New total is {total}")
        return total
    
    @output(id="total")
    @render.text
    def print_total():
        return total()
    
app = App(app_ui, server)

