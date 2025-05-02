from thireteen import get_avg_diff_excl_earliest

avg_diff_excl_earliest = get_avg_diff_excl_earliest()
years = avg_diff_excl_earliest/365  # year
months = avg_diff_excl_earliest/30
print(years, months)
