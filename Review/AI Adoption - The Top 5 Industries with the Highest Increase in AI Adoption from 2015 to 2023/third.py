def get_baseline():
    return {
        'Manufacturing': 12,
        'IT & Telecom': 12,
        'Health Care': 12,
        'Retail': 4,
        'Construction': 4,
        'Financial Services': 55  # baseline 2018 >55; I'll use 55 minimal
    }

def get_adoption_2023():
    return {
        'Manufacturing': 70,
        'IT & Telecom': 63,
        'Health Care': 38,
        'Retail': 79,
        'Construction': 26,
        'Financial Services': 99
    }

def get_increase():
    adoption_2023 = get_adoption_2023()
    baseline = get_baseline()
    return {k: adoption_2023[k]-baseline[k] for k in adoption_2023}

if __name__ == "__main__":
    print(get_increase())
