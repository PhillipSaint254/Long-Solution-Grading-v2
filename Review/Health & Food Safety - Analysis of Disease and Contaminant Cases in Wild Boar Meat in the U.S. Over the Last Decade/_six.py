from five import get_df

df = get_df()
category_freq = df.groupby("type").size().rename("events")
category_cases = df.groupby("type")["human_case_num"].sum()
print(category_freq, category_cases)
