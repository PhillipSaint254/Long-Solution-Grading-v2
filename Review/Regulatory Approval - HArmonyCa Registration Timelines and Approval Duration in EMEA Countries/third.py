from first import get_dates

# consecutive differences in chronological order
def get_ordered_dates():
    dates = get_dates()
    return sorted(dates.items(), key=lambda x: x[1])

if __name__ == "__main__":
    print(get_ordered_dates())
    