from _ten import get_countries, get_data

def get_europe_data():
    data = get_data()
    europe_countries = get_countries()

    # Let's extend the list of countries to include the alternative names present in the data
    europe_aliases = [
        ('Russia', 'Russian Federation'),
        ('Moldova', 'Republic of Moldova'),
        ('North Macedonia', 'Macedonia'),
    ]
    # Now, build a dictionary mapping the table's country name to the desired output
    name_map = {}
    for c in europe_countries:
        name_map[c] = c  # default
    for out_name, in_name in europe_aliases:
        name_map[out_name] = out_name
        # Also add a mapping from in_name to out_name
        name_map[in_name] = out_name

    # Now filter the data for countries that appear in the name_map
    europe_data = []
    for row in data:
        if row[0] in name_map:
            # rename
            clean_name = name_map[row[0]]
            europe_data.append([clean_name] + row[1:])  # use auto
    
    return europe_data

if __name__ == "__main__":
    europe_data = get_europe_data()
    print(len(europe_data))
