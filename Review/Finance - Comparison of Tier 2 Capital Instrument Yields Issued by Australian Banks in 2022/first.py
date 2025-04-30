import pandas as pd, numpy as np

def get_data():
    # create dictionary with bank, issue_date, yield_percent
    return [
        ("NAB", "20 July 2022", 6.150),
        ("Westpac", "10 August 2022", 5.405),
        ("Commonwealth Bank of Australia", "9 November 2022", 6.86),
        ("ANZ Banking Group", "20 September 2022", 6.405)
    ]

def get_df():
    data = get_data()
    return pd.DataFrame(data, columns=["Bank","Issue Date","Yield"])


if __name__ == "__main__":
    df = get_df()
    avg_yield_total = df["Yield"].mean()
    highest_bank = df.loc[df["Yield"].idxmax(), "Bank"]
    lowest_bank = df.loc[df["Yield"].idxmin(), "Bank"]
    print(avg_yield_total, highest_bank, lowest_bank)
