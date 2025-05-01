from ten import get_df

def get_df_table(): 
    df = get_df()
    return df[["year","location","disease_or_contaminant","type","human_case_num","details"]]

if __name__ == "__main__":
    print(get_df_table())
