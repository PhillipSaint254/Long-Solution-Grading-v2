from _six import get_df

def get_sorted_df():
    df = get_df()
    return df.sort_values('Price')

if __name__ == "__main__":
    df_sorted = get_sorted_df()
    print(df_sorted)
