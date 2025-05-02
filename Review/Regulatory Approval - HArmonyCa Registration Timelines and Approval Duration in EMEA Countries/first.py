from datetime import datetime, timedelta, date

def get_dates():
    return {
        'Israel': datetime(2020,10,8),
        'Italy': datetime(2021,4,1), # approx.
        'Monaco/EU': datetime(2022,4,1),
        'UK': datetime(2022,9,21),
        'Ukraine': datetime(2022,9,21),
    }

def get_differences():
    dates = get_dates()
    base = dates['Israel']
    return [(d - base).days for c, d in dates.items() if c != 'Israel']

if __name__ == "__main__":
    print(get_differences())
    