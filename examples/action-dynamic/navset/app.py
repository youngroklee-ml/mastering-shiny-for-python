from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("controller", "Show", choices=[f"panel{x}" for x in range(1, 4)])
        ),
        ui.navset_hidden(
            ui.nav_panel("panel1", "Panel 1 content"),
            ui.nav_panel("panel2", "Panel 2 content"),
            ui.nav_panel("panel3", "Panel 3 content"),
            id="switcher",
        )
    )
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.controller)
    def _():
        ui.update_navs("switcher", selected=input.controller())

app = App(app_ui, server)
