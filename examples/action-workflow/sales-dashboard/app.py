from shiny import App, reactive, render, ui
import pandas as pd

sales = pd.read_csv("sales-dashboard/sales_data_sample.csv", 
                    sep=",", encoding="Latin-1", 
                    na_values=["", "NaN"], keep_default_na=False)
sales = sales[["TERRITORY", "ORDERDATE", "ORDERNUMBER", "PRODUCTCODE", 
               "QUANTITYORDERED", "PRICEEACH"]]

app_ui = ui.page_fluid(
    ui.input_select("territory", "territory", choices=list(sales["TERRITORY"].unique())),
    ui.output_table("selected"),
)


def server(input, output, session):
    @reactive.calc
    def selected():
        return sales[sales["TERRITORY"]==input.territory()]

    @output(id="selected")
    @render.table
    def print_selected():
        return selected()[:11]

app = App(app_ui, server)
