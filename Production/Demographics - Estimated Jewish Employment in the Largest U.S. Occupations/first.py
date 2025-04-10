def get_occupations():
    return {
        "Home Health and Personal Care Aides": 3689350,
        "Retail Salespersons": 3684740,
        "Fast Food and Counter Workers": 3676580,
        "General and Operations Managers": 3507810,
        "Cashiers": 3298660
    }

# constants
def get_pop_total():
    return 7.5e6 # 7.5 million

def get_propotion():
    return 0.024 # 2.4%

def get_results():
    jewish_pop_total = get_pop_total()
    occupations = get_occupations()
    jewish_proportion = get_propotion()
    # compute estimated jewish in each occupation and percentage of total jewish population
    results = []
    for occ, employ in occupations.items():
        jewish_est = employ * jewish_proportion
        percent_of_total = jewish_est / jewish_pop_total * 100
        results.append((occ, employ, jewish_est, percent_of_total))

    return results

if __name__ == "__main__":
    results = get_results()
    print(results)
