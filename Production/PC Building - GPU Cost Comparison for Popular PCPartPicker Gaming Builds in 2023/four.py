from second import get_data
import pandas as pd

def get_df():
    data = get_data()

    df = pd.DataFrame(data)
    df = df.sort_values(by="Total Build Cost ($)", ascending=False)
    df["GPU % of Total"] = df["GPU % of Total"].map(lambda x: round(x,2))
    return df

if __name__ == "__main__":
    df = get_df()
    print(df)
