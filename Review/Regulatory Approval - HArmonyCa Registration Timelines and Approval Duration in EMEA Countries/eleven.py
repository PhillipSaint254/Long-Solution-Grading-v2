from ten import get_avg_days_excl_earliest

avg_days_excl_earliest = get_avg_days_excl_earliest()
avg_months = avg_days_excl_earliest/30
avg_years = avg_days_excl_earliest/365
print(avg_days_excl_earliest, avg_months, avg_years)
