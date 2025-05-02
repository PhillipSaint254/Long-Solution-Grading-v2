from datetime import datetime

def get_dates():
    return {
        'Israel': datetime(2020,10,8),
        'Italy': datetime(2021,4,1),
        'Monaco': datetime(2022,4,1),
        'UK': datetime(2022,9,21),
        'Ukraine': datetime(2022,9,21),
    }

def get_diffs():
    dates = get_dates()
    base = min(dates.values())  # earliest date
    # compute difference from earliest for each
    return {country: (date - base).days for country, date in dates.items()}

if __name__ == "__main__":
    print(get_diffs())
