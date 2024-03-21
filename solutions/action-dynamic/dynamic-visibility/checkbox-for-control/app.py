from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.input_checkbox("advanced", "Advanced"),
    ui.navset_hidden(
        ui.nav_panel("empty"),
        ui.nav_panel("additional",
                     ui.input_numeric("number", "Additional control", 
                                      value=1, min=0, max=10)
        ),
        id="wizard"
    )
)

def server(input, output, session):
    @reactive.effect
    def _():
        ui.update_navs("wizard", 
                       selected="additional" if input.advanced() else "empty")


app = App(app_ui, server)
