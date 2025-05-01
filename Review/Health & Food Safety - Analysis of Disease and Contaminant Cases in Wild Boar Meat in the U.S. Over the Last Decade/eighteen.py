from twelve import get_df_table

def get_freq_table():
    df_table = get_df_table()
    return df_table.groupby("disease_or_contaminant").agg(event_occurrences=("year","count"), human_cases=("human_case_num","sum")).reset_index()

if __name__ == "__main__":
    freq_table = get_freq_table()
    print(freq_table)
    print(freq_table.to_markdown(index=False))
    