from five import get_df_sorted

def get_avg_inflation():
    df_sorted = get_df_sorted()
    return round(df_sorted['Inflation rate (%)'].mean(), 2)

if __name__ == "__main__":
    print(get_avg_inflation())
