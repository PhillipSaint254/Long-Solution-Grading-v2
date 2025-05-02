import requests
import pandas as pd

def get_tables():
    url = "https://www.global-rates.com/en/inflation/cpi/72/israel/"
    return pd.read_html(url)

if __name__ == "__main__":
    tables = get_tables()
    print(len(tables))
