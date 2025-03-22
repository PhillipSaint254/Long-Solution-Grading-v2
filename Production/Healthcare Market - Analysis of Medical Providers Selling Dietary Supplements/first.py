# Compute average and standard deviation for provided percentages

import math

percentages = {
    'Collagen (dermatologists)': 66,
    'Proteins (dietitians)': 97,
    'Fish oil (HCPs)': 88,
    'Beta-alanine (dietitian influence)': 52,
    'Vitamins (physicians)': 79
}

values = list(percentages.values())
mean = sum(values) / len(values)

# population standard deviation
variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = math.sqrt(variance)

print("Percentages:", percentages)
print("Mean:", mean)
print("Standard deviation:", std_dev)

