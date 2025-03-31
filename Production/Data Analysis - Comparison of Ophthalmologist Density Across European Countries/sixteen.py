from _ten import get_data

data = get_data()

print([r for r in data if 'Vatican' in r[0]])