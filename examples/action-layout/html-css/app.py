from shiny import App, ui

app_ui = ui.page_fluid(
    ui.include_css("css/my-style.css"),
    ui.HTML(r"""
        <h1>This is a heading</h1>
        <p class="my-class">This is some text!</p>
        <ul>
            <li>First bullet</li>
            <li>Second bullet</li>
        </ul>        
        """)
)

app = App(app_ui, None)
