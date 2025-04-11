from seven import get_df_combined as get_df_combined_1

def get_df_combined():
    df_combined = get_df_combined_1()
    return df_combined.sort_values('Composite Score', ascending=False)

if __name__ == "__main__":
    df_combined = get_df_combined()
    print(df_combined)
