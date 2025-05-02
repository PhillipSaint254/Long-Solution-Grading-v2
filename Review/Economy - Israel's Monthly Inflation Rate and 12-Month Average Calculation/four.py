from third import get_df

def get_df_sorted():
    df = get_df()
    return df[::-1].reset_index(drop=True)  # ascending from March 2024 to February 2025

if __name__ == "__main__":
    df_sorted = get_df_sorted()
    print(df_sorted)
