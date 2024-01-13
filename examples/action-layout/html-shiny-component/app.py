from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.p(
        "You made ",
        ui.tags.b("$", ui.output_text("amount", inline=True)),
        " in the last ",
        ui.output_text("days", inline=True),
        " days ",
    ),
)

def server(input, output, session):
    @render.text
    def amount():
        return 249
    
    @render.text
    def days():
        return 7

app = App(app_ui, server)
