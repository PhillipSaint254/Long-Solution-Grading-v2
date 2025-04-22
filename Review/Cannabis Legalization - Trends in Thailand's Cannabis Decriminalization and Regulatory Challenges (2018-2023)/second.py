from first import get_counts

def get_years():
    return list(range(2018, 2024))

def get_data():
    data = []
    counts = get_counts()
    years = get_years()
    for year in years:
        year_str = str(year)
        data.append({"Year": year_str, "Number of Articles": counts.get(year_str, 0)})
    return data

if __name__ == "__main__":
    print(get_data())
