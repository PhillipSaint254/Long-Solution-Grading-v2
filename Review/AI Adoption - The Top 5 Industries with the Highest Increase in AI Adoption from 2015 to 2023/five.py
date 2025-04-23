from third import get_adoption_2023, get_baseline

# Data for final table
def get_data():
    baseline = get_baseline()
    adoption_2023 = get_adoption_2023()
    return [{'Industry': ind, '2015/2017 Adoption (%)': baseline[ind], '2023 Adoption (%)': adoption_2023[ind], 'Increase (% points)': adoption_2023[ind] - baseline[ind]} for ind in ['Retail', 'Manufacturing', 'IT & Telecom', 'Financial Services', 'Health Care']]

if __name__ == "__main__":
    print(get_data())
