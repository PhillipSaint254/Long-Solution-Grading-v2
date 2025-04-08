import pandas as pd
from fifth import get_unique_categories

def get_table():
    unique_categories = get_unique_categories()
    return pd.DataFrame({'Industry Category (Seedrs)': unique_categories})

if __name__ == "__main__":
    table = get_table()
    print(table)
