from shiny import App, ui

app_ui = ui.page_fluid(
    ui.include_css("css/my-style.css"),
    ui.h1("This is heading"),
    ui.p("This is some text", class_="my-class"),
    ui.tags.ul(
        ui.tags.li("First bullet"),
        ui.tags.li("Second bullet"),
    ),
)

app = App(app_ui, None)
