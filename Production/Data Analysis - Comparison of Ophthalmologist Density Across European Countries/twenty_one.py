from _twenty import get_europe_data

europe_data = get_europe_data()

# Verify a few
for name in ['Germany','United Kingdom','France','Spain','Italy','Greece']:
    row = next(r for r in europe_data if r[0]==name)
    print(row)
