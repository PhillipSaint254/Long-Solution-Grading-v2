from seven import get_df_sorted as get_df_sorted_1

def get_df_sorted():
    df_sorted = get_df_sorted_1()
    df_sorted['Team (Season)'] = df_sorted.apply(lambda row: f"{row['Team']} ({row['Season']})", axis=1)
    return df_sorted

if __name__ == "__main__":
    df_sorted = get_df_sorted()
    print(df_sorted)
