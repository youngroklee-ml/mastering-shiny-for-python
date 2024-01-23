from shiny import App, ui, reactive

modal_confirm = ui.modal(
    "Are you sure you want to continue?",
    title="Delete files",
    footer=ui.TagList(
        ui.modal_button("Cancel"),
        ui.input_action_button("ok", "Delete", class_="btn btn-danger"),
    )
)

app_ui = ui.page_fluid(
    ui.input_action_button("delete", "Delete all files?"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.delete)
    def delete():
        ui.modal_show(modal_confirm)
    
    @reactive.effect
    @reactive.event(input.ok)
    def ok():
        ui.notification_show("Files deleted")
        ui.modal_remove()

app = App(app_ui, server)

