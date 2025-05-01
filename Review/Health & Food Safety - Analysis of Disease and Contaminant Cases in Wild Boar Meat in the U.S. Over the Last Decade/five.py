from four import get_df

df = get_df()
freq = df.groupby("disease_or_contaminant").size().rename("events")
cases = df.set_index("disease_or_contaminant")["human_case_num"]
print(freq, cases)
