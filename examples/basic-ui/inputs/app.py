from shiny import App, ui, render
from faicons import icon_svg

state_names=[
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
    "West Virginia", "Wisconsin", "Wyoming"]

animals = ["dog", "cat", "mouse", "bird", "other", "I hate animals"]

app_ui = ui.page_fluid(
    # free text
    ui.input_text("name", "What's your name?"),
    ui.input_password("password", "What's your password?"),
    ui.input_text_area("story", "Tell me about yourself", rows=3),

    # numeric inputs
    ui.input_numeric("num", "Number one", value=0, min=0, max=100),
    ui.input_slider("num2", "Number two", value=50, min=0, max=100),
    ui.input_slider("rng", "Range", value=(10, 20), min=0, max=100),

    # dates
    ui.input_date("dob", "When were you born?"),
    ui.input_date_range("holiday", "When do you want to go on vacation next?"),

    # limited choices
    ui.input_select("state", "What's your favourite states?", choices=state_names),
    ui.input_radio_buttons("animal", "What's your favourite animals?", choices=animals),
    ui.input_radio_buttons("rb", "Choose one:", choices={
        "angry": icon_svg("face-angry"), "happy": icon_svg("face-smile"), "sad": icon_svg("face-sad-tear")}),
    ui.input_selectize("states", "What's your favourite states?", choices=state_names, multiple=True),
    ui.input_checkbox_group("animals", "What animals do you like?", choices=animals),
    ui.input_checkbox("cleanup", "Clean up?", value=True),
    ui.input_checkbox("shutdown", "Shutdown?"),

    # file uploads
    ui.input_file("upload", None),

    # action buttons
    ui.input_action_button("click", "Click me!"),
    ui.input_action_button("drink", "Drink me!", icon=icon_svg("martini-glass-citrus")),
    ui.br(),
    ui.input_action_button("clickdanger", "Click me!", class_="btn-danger"),
    ui.input_action_button("drinklarge", "Drink me!", class_="btn-lg btn-success"),
    ui.br(),
    ui.input_action_button("eat", "Eat me!", class_="w-100"),
    # output
    ui.output_text("txt")
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return input.drinklarge()

app = App(app_ui, server)
