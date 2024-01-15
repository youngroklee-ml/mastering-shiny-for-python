from shiny import App, ui, render, req

app_ui = ui.page_fluid(
    ui.input_select("language", "Language", choices=["", "English", "Maori"]),
    ui.input_text("name", "Name"),
    ui.output_text("greeting"),
)

def server(input, output, session):
    greetings = {
        'English': "Hello",
        'Maori': "Ki ora",
    }

    @render.text
    def greeting():
        req(input.language(), input.name())
        return f"{greetings[input.language()]} {input.name()}!"
    

app = App(app_ui, server)