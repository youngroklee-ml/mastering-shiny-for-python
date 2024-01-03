from urllib.request import urlretrieve
import os

os.mkdir("neiss")

def download(name):
    url = f"https://github.com/hadley/mastering-shiny/raw/main/neiss/{name}"
    filename = f"neiss/{name}"
    urlretrieve(url, filename)

download("injuries.tsv.gz")
download("population.tsv")
download("products.tsv")

