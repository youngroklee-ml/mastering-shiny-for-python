from shiny import App, ui, render, reactive, req
import numpy as np

app_ui = ui.page_fluid(
    ui.input_numeric("x", "x", value=0),
    ui.input_select("trans", "transformation", choices=["square", "log", "square-root"]),
    ui.output_ui("out_container"),
)

def server(input, output, session):
    @render.ui
    def out_container():
        if input.x() < 0 and input.trans() in ["log", "square-root"]:
            return ui.markdown("**x can not be negative for this transformation**")
        else:
            return ui.output_text("out")
    
    @render.text
    def out():
        req(not (input.x() < 0 and input.trans() in ["log", "square-root"]))
        match input.trans():
            case "square":
                res = input.x()**2
            case "square-root":
                res = np.sqrt(input.x())
            case "log":
                res = np.log(input.x())

        return res

app = App(app_ui, server)
