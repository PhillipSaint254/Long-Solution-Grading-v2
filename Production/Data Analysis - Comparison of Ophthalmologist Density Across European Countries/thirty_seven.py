from twenty_two import get_df_sorted

df_sorted = get_df_sorted()

# Prepare the table for output
out_df = df_sorted[['Country','Total','Population','Oph_per_100k']].copy()
out_df.columns = ['Country','Number of Ophthalmologists','Population','Ophthalmologists per 100,000 people']
out_df['Ophthalmologists per 100,000 people'] = out_df['Ophthalmologists per 100,000 people'].round(2)

# Also convert numbers to int for output
out_df['Number of Ophthalmologists'] = out_df['Number of Ophthalmologists'].astype(int)
out_df['Population'] = out_df['Population'].astype(int)

# Display
print(out_df.head(10).to_markdown(index=False))
