from shiny import App, ui, render, reactive, req
import pandas as pd

app_ui = ui.page_fluid(
    ui.output_ui("interaction_slider"),
    ui.output_text_verbatim("breaks"),
)

def server(input, output, session):
    timeSeries = pd.DataFrame({
        'dateTime': pd.to_datetime([
            "2019-08-20 16:00:00",
            "2019-08-20 16:00:01",
            "2019-08-20 16:00:02",
            "2019-08-20 16:00:03",
            "2019-08-20 16:00:04",
            "2019-08-20 16:00:05"
        ]),
        'var1': [9, 8, 11, 14, 16, 1],
        'var2': [3, 4, 15, 12, 11, 19],
        'var3': [2, 11, 9, 7, 14, 1]
    }).set_index('dateTime')

    @render.ui
    def interaction_slider():
        return ui.input_slider("slider", "Select Range:",
                               min=min(timeSeries.index), max=max(timeSeries.index),
                               value=(min, max)) # (min(datetimes), max(datetimes))
    
    @reactive.calc
    def brks():
        req(input.slider())
        return pd.date_range(input.slider()[0], input.slider()[1], periods=10)
    
    @render.text
    def breaks():
        return brks()
        
app = App(app_ui, server)
