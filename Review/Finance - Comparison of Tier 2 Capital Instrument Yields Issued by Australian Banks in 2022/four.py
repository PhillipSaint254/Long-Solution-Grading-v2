import pandas as pd, numpy as np

def get_data():
    return [
        ("National Australia Bank (NAB)", "20 July 2022", 6.150),
        ("Westpac Banking Corporation", "10 August 2022", 5.405),
        ("Commonwealth Bank of Australia (CBA)", "9 November 2022", 6.86),
        ("Australia & New Zealand Banking Group (ANZ)", "20 September 2022", 6.405)
    ]

def get_df():
    data = get_data()
    return pd.DataFrame(data, columns=["Bank","Issue Date","Yield"])

if __name__ == "__main__":
    print(get_df())
    