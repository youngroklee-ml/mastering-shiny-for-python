from shiny import App, ui, render
from pydataset import data
from scipy.stats import ttest_ind
# from statsmodels.stats.weightstats import ttest_ind
import statsmodels.formula.api as smf

mtcars = data("mtcars")

app_ui = ui.page_fluid(
    ui.output_text_verbatim("summary"),
    ui.output_text("greeting"),
    ui.output_text_verbatim("ttest"),
    ui.output_text_verbatim("regression"),
)

def server(input, output, session):
    @output
    @render.text
    def summary():
        return mtcars.describe()
    
    @output
    @render.text
    def greeting():
        return "Good morning!"
    
    @output
    @render.text
    def ttest():
        return ttest_ind([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    
    @output
    @render.text
    def regression():
        reg = smf.ols("mpg ~ wt", data=mtcars).fit()
        return reg.summary()

app = App(app_ui, server)
