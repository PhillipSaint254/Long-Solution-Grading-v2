from third import get_increase

def get_sorted_increase():
    increase = get_increase()
    return sorted(increase.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print(get_sorted_increase())
