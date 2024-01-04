from shiny import App, ui, render, reactive
import pandas as pd
from plotnine import ggplot, geom_line, aes, labs
import numpy as np

# data load
injuries = pd.read_table(
    "neiss/injuries.tsv.gz", 
    delimiter="\t", 
    compression="gzip",
    parse_dates=['trmt_date']
)
products = pd.read_table("neiss/products.tsv")
population = pd.read_table("neiss/population.tsv")

prod_codes = dict(zip(products['prod_code'], products['title']))

def count_top(df, var, n=5):
    df = df.copy()
    freq = df.value_counts(var)[:n].index.values
    df[var] = pd.Categorical(np.where(np.isin(df[var], freq), df[var], "Other"), 
                             categories=list(freq)+["Other"], ordered=True)
    res = df.groupby([var], observed=False).agg(n=('weight', 'sum')).reset_index()
    res['n'] = res['n'].astype(np.int64)
    return res

app_ui = ui.page_fluid(
    ui.row(
        ui.column(8,
            ui.input_select("code", "Product", choices=prod_codes, width="100%"),
        ),
        ui.column(2, 
            ui.input_select("y", "Y axis", choices=["rate", "count"]),
        ),
        ui.column(2,
            ui.input_numeric("n", "Top N values", value=5, min=1),
        ),
    ),
    ui.row(
        ui.column(4, ui.output_table("diag")),
        ui.column(4, ui.output_table("body_part")),
        ui.column(4, ui.output_table("location")),
    ),
    ui.row(
        ui.column(12, ui.output_plot("age_sex")),
    ),
    ui.row(
        ui.column(1, ui.input_action_button("backward", "Prev")),
        ui.column(1, ui.input_action_button("forward", "Next")),
        ui.column(10, ui.output_text("narrative")),
    ),    
)

def server(input, output, session):
    @reactive.calc
    def selected():
        return injuries[injuries['prod_code']==int(input.code())].copy()
    
    @render.table(classes='table shiny-table w-100')
    def diag():
        return count_top(selected(), 'diag', n=input.n())

    @render.table(classes='table shiny-table w-100')
    def body_part():
        return count_top(selected(), 'body_part', n=input.n())

    @render.table(classes='table shiny-table w-100')
    def location():
        return count_top(selected(), 'location', n=input.n())

    @reactive.calc
    def summary():
        res = selected().groupby(['age', 'sex']).agg(n=('weight', 'sum')).reset_index().\
            merge(population, how='left', on=['age', 'sex'])
        res['rate'] = res['n'] / res['population'] * 1e4

        return res
    
    @render.plot
    def age_sex():
        if input.y()=="count":
            res = (ggplot(summary(), aes('age', 'n', colour='sex'))
                   + geom_line(na_rm=True)
                   + labs(y="Estimated number of injuries"))
        else:
            res = (ggplot(summary(), aes('age', 'rate', colour='sex'))
                   + geom_line(na_rm=True)
                   + labs(y="Injuries per 10,000 people"))

        return res
    
    current = reactive.value(0)

    @reactive.effect
    @reactive.event(selected)
    def _():
        current.set(0)

    @reactive.effect
    @reactive.event(input.backward)
    def _():
        if current() > 0:
            current.set(current() - 1)
        else:
            current.set(selected().shape[0] - 1)
    
    @reactive.effect
    @reactive.event(input.forward)
    def _():
        if current() < selected().shape[0] - 1:
            current.set(current() + 1)
        else:
            current.set(0)

    @render.text
    def narrative():
        return selected()['narrative'].values[current()]
    

app = App(app_ui, server)
