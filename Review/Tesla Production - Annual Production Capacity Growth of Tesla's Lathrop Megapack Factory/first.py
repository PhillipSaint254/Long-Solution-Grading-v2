# We need to prepare a table of years and production capacity (GWh per year).
# Data:
# 2022: 20 GWh (assumed)
# 2023: 20 GWh (assumed)
# 2024: 40 GWh (per 2024 source)
# We want YOY growth percentages.

years = [2022, 2023, 2024]
capacities = [20, 20, 40]

# Compute YOY growth = ((current - previous) / previous) * 100.
growths = [None]  # For first year we can't compute.
for i in range(1, len(capacities)):
    prev = capacities[i-1]
    curr = capacities[i]
    growth = (curr - prev) / prev * 100
    growths.append(growth)

# Format results in a simple table-like structure.
print(list(zip(years, capacities, growths)))

