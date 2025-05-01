from twelve import get_df_table
# We'll create final dataset for output.
def get_final_table():
    df_table = get_df_table()
    return df_table.rename(columns={
        "year":"Year",
        "location":"Location / Source",
        "disease_or_contaminant":"Disease or contaminant",
        "type":"Category",
        "human_case_num":"Human cases",
        "details":"Notes"
    })

if __name__ == "__main__":
    print(get_final_table())
