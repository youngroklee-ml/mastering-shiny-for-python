from shiny import App, ui, reactive, render, req

app_ui = ui.page_fluid(
    ui.input_text("label", "label"),
    ui.input_select("type", "type", choices=("slider", "numeric")),
    ui.output_ui("numeric"),
)

def server(input, output, session):
    @render.ui
    def numeric():
        with reactive.isolate():
            try:
                value = input.dynamic()
            except:
                value = 0

        if input.type() == "slider":
            res = ui.input_slider("dynamic", input.label(), value=value, min=0, max=10)
        else:
            res = ui.input_numeric("dynamic", input.label(), value=value, min=0, max=10)

        return res

app = App(app_ui, server)
