from shiny import App, ui, reactive, render
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_numeric("n", "Number of colours", value=5, min=1),
            ui.output_ui("col"),
        ),
        ui.output_plot("plot"),
    )
)

def server(input, output, session):
    @reactive.calc
    def col_names():
        return [f"col{x}" for x in range(1, input.n() + 1)]
    
    @render.ui
    def col():
        with reactive.isolate():
            values = {}
            for x in col_names():
                try:
                    values[x] = input[x]()
                except:
                    values[x] = ""

        return [ui.input_text(x, None, value=values[x]) for x in col_names()]
 
    @reactive.calc
    def palette():
        return [input[x]() for x in col_names()]
    
    @render.plot
    def plot():
        cols = [x if is_color_like(x) else "none" for x in palette()]

        fig, ax = plt.subplots()

        ax.bar(x=col_names(), height=1, width=1, color=cols, edgecolor='grey')
        ax.set_axis_off()

        return ax

    
app = App(app_ui, server)
