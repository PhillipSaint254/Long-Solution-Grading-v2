from seven import get_df_sorted, get_avg_inflation
import pandas as pd

def get_df_final():
    df_sorted = get_df_sorted()
    avg_inflation = get_avg_inflation()
    return pd.concat([df_sorted, pd.DataFrame([['Average for last 12 months', avg_inflation]], columns=['Month', 'Inflation rate (%)'])], ignore_index=True)

if __name__ == "__main__":
    df_final = get_df_final()
    print(df_final)
