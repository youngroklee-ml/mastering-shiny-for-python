from shiny import App, ui, reactive, render
from gapminder import gapminder

continents = gapminder['continent'].unique().tolist()

app_ui = ui.page_fluid(
    ui.input_select("continent", "Continent", choices=["(All)"] + continents),
    ui.input_select("country", "Country", choices=list()),
    ui.output_table("data"),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.continent)
    def _():
        if input.continent() == "(All)":
            countries = gapminder['country'].unique().tolist()
        else:
            countries = gapminder[gapminder['continent']==input.continent()]['country'].unique().tolist()
        ui.update_select("country", choices=countries)

    @reactive.calc
    def country():
        return gapminder[gapminder['country']==input.country()]
    
    @render.table
    def data():
        return country()

app = App(app_ui, server)

