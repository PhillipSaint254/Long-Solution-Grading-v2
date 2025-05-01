from seven import get_summary_table

def get_specific_freq():
    summary_table = get_summary_table()
    return summary_table.groupby("disease_or_contaminant").agg(events=("year","count"), cases=("human_case_num","sum"))

if __name__ == "__main__":
    print(get_specific_freq())
