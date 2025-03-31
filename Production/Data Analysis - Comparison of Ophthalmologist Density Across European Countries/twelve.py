from _ten import get_data

data = get_data()

# Look for 'Macedonia'
print([r for r in data if 'Macedonia' in r[0]])
