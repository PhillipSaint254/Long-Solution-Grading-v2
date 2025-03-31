from _ten import get_data

data = get_data()

# Look for "Russian" in countries
print([r for r in data if 'Russia' in r[0]])
