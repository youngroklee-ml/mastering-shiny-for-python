from shiny import App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_action_button("go", "Enter password"),
    ui.output_text("text"),
)


def server(input, output, session):
    pw = reactive.value('')

    @reactive.effect
    @reactive.event(input.go)
    def _():
        m = ui.modal(
            ui.input_password("password", "Password: ", value=pw.get()),
            ui.input_action_button("submit", "Submit"),
            title="Please enter your password",
            footer=None,
        )
        ui.modal_show(m)

    @reactive.calc
    @reactive.event(input.submit)
    def get_password():
        res = input.password()
        pw.set(res)
        ui.modal_remove()
        return res

    @render.text
    def text():
        if get_password()=="":
            return "No password"
        
        return "Password entered"


app = App(app_ui, server)
