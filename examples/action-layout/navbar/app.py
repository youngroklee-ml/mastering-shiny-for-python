from shiny import App, ui

app_ui = ui.page_navbar(
    ui.nav_control(ui.h4("Page title")),
    ui.nav_panel("panel 1", "one"),
    ui.nav_panel("panel 2", "two"),
    ui.nav_panel("panel 3", "three"),
    ui.nav_menu("subpanels",
        ui.nav_panel("panel 4a", "four-a"),
        ui.nav_panel("panel 4b", "four-b"),
        ui.nav_panel("panel 4c", "four-c"),
    ),
)

app = App(app_ui, None)
