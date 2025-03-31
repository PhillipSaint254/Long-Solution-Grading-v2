from _ten import get_data

data = get_data()

print([r for r in data if 'Andorra' in r[0]])