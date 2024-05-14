from shiny import App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_select("type", "type", ["slider", "numeric"]),
    ui.navset_hidden(
        ui.nav_panel("slider",
                     ui.input_slider("n_slider", "n", value=0, min=0, max=100)),
        ui.nav_panel("numeric",
                     ui.input_numeric("n_numeric", "n", value=0, min=0, max=100)),
        id="wizard",
    ),
)


def server(input, output, session):
    @reactive.effect
    def _():
        ui.update_navs("wizard", selected=input.type())
    
    @reactive.effect
    @reactive.event(input.n_slider)
    def _():
        ui.update_numeric("n_numeric", value=input.n_slider())

    @reactive.effect
    @reactive.event(input.n_numeric)
    def _():
        ui.update_slider("n_slider", value=input.n_numeric())
    

app = App(app_ui, server)
