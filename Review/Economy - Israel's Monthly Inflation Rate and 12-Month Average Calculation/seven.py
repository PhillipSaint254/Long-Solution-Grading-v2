from five import get_df_sorted as gdfs

def get_df_sorted():
    df_sorted = gdfs()
    df_sorted['Inflation rate (%)'] = df_sorted['Inflation rate (%)'].round(2)
    return df_sorted

def get_avg_inflation():
    df_sorted = get_df_sorted()
    avg_inflation = df_sorted['Inflation rate (%)'].mean().round(2)
    return avg_inflation

if __name__ == "__main__":
    print(get_avg_inflation())
