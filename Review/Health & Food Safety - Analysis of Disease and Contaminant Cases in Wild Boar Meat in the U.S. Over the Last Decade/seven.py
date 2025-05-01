from five import get_df

def get_summary_table():
    df = get_df()
    return df[["year", "disease_or_contaminant", "type", "human_case_num"]]

if __name__ == "__main__":
    print(get_summary_table())
    