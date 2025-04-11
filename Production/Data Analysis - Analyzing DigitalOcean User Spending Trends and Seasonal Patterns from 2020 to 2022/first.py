import pandas as pd

def get_months():
    return pd.date_range(start='2020-01-01', end='2022-12-31', freq='MS')  # monthly start

if __name__ == "__main__":
    months = get_months()
    print(len(months))
