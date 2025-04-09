from seven import get_sorted_df as get_sorted_df_7

def get_sorted_df():
    df_sorted = get_sorted_df_7()
    df_sorted['Price_USD'] = df_sorted['Price'].map(lambda x: f"${x:,.2f}")
    df_sorted.drop(columns=['Price'], inplace=True)
    return df_sorted

if __name__ == "__main__":
    df_sorted = get_sorted_df()
    print(df_sorted)
