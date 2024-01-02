from shiny import App, ui, render, reactive

app_ui = ui.page_fluid(
    ui.input_text("name", "What's your name?"),
    ui.output_text("greeting"),
)

def server(input, output, session):
    @reactive.calc
    def string():
        return f"Hello {input.name()}!"

    @render.text
    def greeting():
        return string()
    
app = App(app_ui, server)
