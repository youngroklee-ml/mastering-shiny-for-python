from shiny import App, ui

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Import data",
            ui.input_file("file", "Data", button_label="Upload..."),
            ui.input_text("delim", "Delimiter (leave blank to guess)", ""),
            ui.input_numeric("skip", "Rows to skip", 0, min=0),
            ui.input_numeric("rows", "Rows to preview", 10, min=1),
        ),
        ui.nav_panel("Set parameters"),
        ui.nav_panel("Visualise results"),
    )
)

def server(input, output, session):
    ...

app = App(app_ui, server)
