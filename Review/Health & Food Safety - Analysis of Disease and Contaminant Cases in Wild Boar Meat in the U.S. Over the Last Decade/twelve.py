from ten import get_df as gdf

def get_df():
    df = gdf()
    df["details"] = ["144,000 pounds recalled due to undeclared soy allergen", 
                 "4,692 pounds recalled due to nitrite above limit",
                 "12 human cases of trichinellosis from raw boar meat",
                 "1 human case of brucellosis linked to feral swine meat"]
    return df

def get_df_table():
    df = get_df()
    return df[["year","location","disease_or_contaminant","type","human_case_num","details"]]

if __name__== "__main__":
    print(get_df_table())
