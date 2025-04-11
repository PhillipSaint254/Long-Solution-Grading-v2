import pandas as pd
from four import get_data

def get_df():
    data = get_data()
    return pd.DataFrame(data)

def get_monthly_avg():
    df = get_df()
    # compute monthly average across 100 users
    return df.groupby('date')['spend'].mean()

if __name__ == "__main__":
    monthly_avg = get_monthly_avg()
    print(monthly_avg.head(), monthly_avg.tail())
