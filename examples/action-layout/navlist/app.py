from shiny import App, ui

app_ui = ui.page_fluid(
    ui.navset_pill_list(
        ui.nav_control(
            ui.h3("Heading 1")
        ),
        ui.nav_panel("panel 1", "Panel one contents"),
        ui.nav_control(
            ui.h3("Heading 2")
        ),
        ui.nav_panel("panel 2", "Panel two contents"),
        ui.nav_panel("panel 3", "Panel three contents"),
        id="tabset",
    ),
)

app = App(app_ui, None)
