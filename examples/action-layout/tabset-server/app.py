from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.output_text("panel"),
        ),
        ui.navset_tab(
            ui.nav_panel("panel 1", "one"),
            ui.nav_panel("panel 2", "two"),
            ui.nav_panel("panel 3", "three"),
            id="tabset",
        ),
    ),
)

def server(input, output, session):
    @render.text
    def panel():
        return f"Current panel: {input.tabset()}"

app = App(app_ui, server)
