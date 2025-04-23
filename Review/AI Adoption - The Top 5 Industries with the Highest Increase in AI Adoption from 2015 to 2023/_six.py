from third import get_adoption_2023, get_baseline

def get_relative_growth():
    adoption_2023 = get_adoption_2023()
    baseline = get_baseline()
    return {k: (adoption_2023[k] - baseline[k]) / baseline[k] * 100 for k in baseline}


if __name__ == "__main__":
    print(get_relative_growth())
