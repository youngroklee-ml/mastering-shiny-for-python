from shiny import App, ui, reactive

app_ui = ui.page_fluid(
    ui.navset_hidden(
        ui.nav_panel("page_1",
                     "Welcome!",
                     ui.input_action_button("page_12", "next")
        ),
        ui.nav_panel("page_2",
                     "Only one page to go",
                     ui.input_action_button("page_21", "prev"),
                     ui.input_action_button("page_23", "next")
        ),
        ui.nav_panel("page_3",
                     "You're done!",
                     ui.input_action_button("page_32", "prev")
        ),
        id="wizard"
    )
)

def server(input, output, session):
    def switch_page(i):
        ui.update_navs("wizard", selected=f"page_{i}")
    
    @reactive.effect
    @reactive.event(input.page_12)
    def _():
        switch_page(2)

    @reactive.effect
    @reactive.event(input.page_21)
    def _():
        switch_page(1)

    @reactive.effect
    @reactive.event(input.page_23)
    def _():
        switch_page(3)

    @reactive.effect
    @reactive.event(input.page_32)
    def _():
        switch_page(2)

app = App(app_ui, server)
