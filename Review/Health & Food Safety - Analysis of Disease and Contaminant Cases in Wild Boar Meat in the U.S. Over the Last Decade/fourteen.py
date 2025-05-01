from twelve import get_df_table

def get_specific_freq():
    df_table = get_df_table()
    return df_table.groupby("disease_or_contaminant").agg(event_count=("year","count"), human_cases=("human_case_num","sum"))

if __name__ == "__main__":
    print(get_specific_freq())
