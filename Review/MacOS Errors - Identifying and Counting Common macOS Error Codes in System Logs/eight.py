import pandas as pd
from seven import get_data

def get_df():
    data = get_data()
    df = pd.DataFrame(data).sort_values("Error Code")
    return df

if __name__ == "__main__":
    print(get_df())
    