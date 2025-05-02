from nine import get_differences

def get_avg_days_excl_earliest():
    differences = get_differences()
    return sum([d for d in differences if d>0]) / (len(differences)-1)

if __name__ == "__main__":
    print(get_avg_days_excl_earliest())
