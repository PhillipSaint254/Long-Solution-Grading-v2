from _ten import get_data

data = get_data()

print([r for r in data if 'Mold' in r[0]])
