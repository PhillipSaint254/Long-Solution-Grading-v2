from datetime import datetime

def get_dates():
    return {
        'Israel': datetime(2020,10,8),
        'Italy': datetime(2021,4,1),
        'Monaco/EU': datetime(2022,4,1),
        'UK': datetime(2022,9,21),
        'Ukraine': datetime(2022,9,21)
    }

def get_differences():
    dates = get_dates()
    base = dates['Israel']
    return [(date - base).days for date in dates.values()]

def get_avg_days():
    differences = get_differences()
    return sum(differences)/len(differences) # including Israel difference 0

if __name__ == "__main__":
    print(get_avg_days())
