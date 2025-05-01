from twelve import get_df_table

def get_summary():
    df_table = get_df_table()
    return df_table.groupby("type").agg(events=("year","count"), human_cases=("human_case_num","sum"))

if __name__ == "__main__":
    print(get_summary())
