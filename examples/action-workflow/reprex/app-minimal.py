from shiny import App, ui, render, reactive, req
from datetime import datetime, timedelta
import pandas as pd

datetimes = pd.DatetimeIndex(map(lambda x: datetime.now() + timedelta(days=x), range(11)))

app_ui = ui.page_fluid(
    ui.input_slider("slider", "Select Range:",
                    min=min(datetimes), max=max(datetimes),
                    value=(min, max)), # (min(datetimes), max(datetimes))
    ui.output_text_verbatim("breaks"),
)

def server(input, output, session):
    @reactive.calc
    def brks():
        req(input.slider())
        return pd.date_range(input.slider()[0], input.slider()[1], periods=10)
    
    @render.text
    def breaks():
        return brks()
        
app = App(app_ui, server)
