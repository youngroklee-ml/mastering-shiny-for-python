from shiny import App, ui, render
from shiny.types import ImgData
import pandas as pd

puppies = pd.DataFrame({
    'breed': ["corgi", "labrador", "spaniel"],
    'id': ["eoqnr8ikwFE", "KCdYn0xu2fU", "TzjMd7i5WQI"],
    'author': ["alvannee", "shaneguymon", "_redo_"],
})

app_ui = ui.page_fluid(
    ui.input_select("id", "Pick a breed", 
                    choices=dict(zip(puppies['id'], puppies['breed']))),
    ui.output_ui("source"),
    ui.output_image("photo"),
)

def server(input, output, session):
    @render.image
    def photo():
        img: ImgData = {"src": f"puppy-photos/{input.id()}.jpg", 
                        "width": "500px", "height": "650px"}
        return img
    
    @render.ui
    def source():
        info = puppies[puppies['id'] == input.id()]
        res = ui.HTML(f"""<p>
            <a href='https://unsplash.com/photos/{info['id'].squeeze()}'>original</a> by
            <a href='https://unsplash.com/@{info['author'].squeeze()}'>{info['author'].squeeze()}</a>
            </p>""")
        
        return res

app = App(app_ui, server)
