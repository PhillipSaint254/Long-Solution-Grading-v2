from eight import get_df_sorted

# final table to show
def get_final_table():
    df_sorted = get_df_sorted()
    return df_sorted[['Team (Season)', 'BattingAverage', 'ERA', 'FieldingPct']]

if __name__ == "__main__":
    final_table = get_final_table()
    print(final_table)
    