from shiny import App, ui, render, reactive
from pydataset import data
import seaborn as sns

app_ui = ui.page_fluid(
    ui.input_select("dataset", label="Dataset", choices=list(data()['dataset_id'])),
    ui.output_text_verbatim("summary"),
    ui.output_plot("plot")
)

def server(input, output, session):
    # Create a reactive expression
    @reactive.calc
    def dataset():
        return data(input.dataset())    

    @output
    @render.text
    def summary():
        return dataset().describe()
    
    @output
    @render.plot
    def plot():
        return sns.pairplot(dataset())

app = App(app_ui, server)
