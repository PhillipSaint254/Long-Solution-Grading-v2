from five import get_df

def get_df_sorted():
    df = get_df()
    return df.sort_values(by='Season', ascending=False).reset_index(drop=True)

if __name__ == "__main__":
    df_sorted = get_df_sorted()
    print(df_sorted)
