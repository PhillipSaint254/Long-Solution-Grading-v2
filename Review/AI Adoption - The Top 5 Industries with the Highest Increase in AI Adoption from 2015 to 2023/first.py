# We'll compute difference for each industry
def get_baseline_2017():
    return {
        'Manufacturing': 12,
        'Information (IT/Telecom)': 12, # information services includes IT
        'Health Care': 12,
        'Construction': 4,
        'Retail': 4,
    }

def get_adoption_2023():
    return {
        'Manufacturing': 70,
        'Information (IT/Telecom)': 63,
        'Health Care': 38,  # 38% of physicians used AI in 2023 according to AMA article
        'Construction': 26,
        'Retail': 79,
    }


# compute increases
def get_increases():
    adoption_2023 = get_adoption_2023()
    baseline_2017 = get_baseline_2017()
    return {industry: adoption_2023[industry] - baseline_2017.get(industry, 0) for industry in adoption_2023}


if __name__ == "__main__":
    print(get_increases())
