from shiny import App, ui

grouped = {
    "Group A": {"A1":"Item A1", "A2":"Item A2"},
    "Group B": {"B1":"Item B1", "B2":"Item B2", "B3":"Item B3"},
    "Group C": {"C1":"Item C1", "C2":"Item C2"}
}

app_ui = ui.page_fluid(
    ui.input_select("long", "Choose:", choices=grouped),
)

def server(input, output, session):
    ...

app = App(app_ui, server)
