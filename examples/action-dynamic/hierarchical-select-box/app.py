from shiny import App, ui, reactive, req, render
import pandas as pd

sales = pd.read_csv("sales-dashboard/sales_data_sample.csv",
                    sep=",", encoding="Latin-1", 
                    na_values=["", "NaN"], keep_default_na=False)

app_ui = ui.page_fluid(
    ui.input_select("territory", "Territory", choices=sales['TERRITORY'].unique().tolist()),
    ui.input_select("customername", "Customer", choices=list()),
    ui.input_select("ordernumber", "Order number", choices=list()),
    ui.output_table("data"),
)

def server(input, output, session):
    @reactive.calc
    def territory():
        return sales[sales['TERRITORY']==input.territory()]
    
    @reactive.effect
    @reactive.event(territory)
    def _():
        choices = territory()['CUSTOMERNAME'].unique().tolist()
        ui.update_select("customername", choices=choices)

    @reactive.calc
    def customer():
        req(input.customername())
        return territory()[territory()['CUSTOMERNAME']==input.customername()]
    
    @reactive.effect
    @reactive.event(customer)
    def _():
        choices = customer()['ORDERNUMBER'].unique().tolist()
        ui.update_select("ordernumber", choices=choices)
    
    @render.table
    def data():
        req(input.ordernumber())
        res = customer()[customer()['ORDERNUMBER']==int(input.ordernumber())]\
            [['QUANTITYORDERED', 'PRICEEACH', 'PRODUCTCODE']]
        
        return res


app = App(app_ui, server)
