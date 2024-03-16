# Please download county.csv from https://www.openintro.org/data/
# and store it to data/ folder
# before running this app

from shiny import App, ui, reactive
import pandas as pd

df = pd.read_csv("data/county.csv")
states = df['state'].unique().tolist()

app_ui = ui.page_fluid(
    ui.input_select("state", "State", choices=states),
    ui.input_select("county", "County", choices=list()),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.state)
    def _():
        county_label = "County"
        if input.state()=="Louisiana":
            county_label = "Parish"
        elif input.state()=="Alaska":
            county_label = "Borough"

        counties = df[df['state']==input.state()]['name'].to_list()
        ui.update_select("county", label=county_label, choices=counties)


app = App(app_ui, server)
