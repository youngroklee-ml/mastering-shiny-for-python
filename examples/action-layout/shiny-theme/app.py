from shiny import App, ui
import shinyswatch

app_ui = ui.page_fluid(
    shinyswatch.theme.darkly(),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_text("txt", "Text input:", "text here"),
            ui.input_slider("slider", "Slider input:", min=1, max=100, value=30),
        ),
        ui.h1("Theme: darkly"),
        ui.h2("Header 2"),
        ui.p("Some text"),
    ),
)

app = App(app_ui, None)
