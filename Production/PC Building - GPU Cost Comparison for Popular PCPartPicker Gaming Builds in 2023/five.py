from second import get_data
import pandas as pd

def get_df():
    data = get_data()
    df = pd.DataFrame(data)
    df['GPU % of Total'] = (df['GPU % of Total']).apply(lambda x: round(x,2))
    df = df.sort_values('Total Build Cost ($)', ascending=False)
    return df

if __name__ == "__main__":
    df = get_df()
    print(df)
