from urllib.request import urlretrieve
import os

os.mkdir("sales-dashboard")

urlretrieve(
    "https://github.com/hadley/mastering-shiny/raw/main/sales-dashboard/sales_data_sample.csv", 
    "sales-dashboard/sales_data_sample.csv"
)
