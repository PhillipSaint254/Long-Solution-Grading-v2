from third import get_ordered_dates

def get_consecutive_diffs():
    ordered_dates = get_ordered_dates()
    consecutive_diffs = []
    for i in range(1, len(ordered_dates)):
        diff = (ordered_dates[i][1] - ordered_dates[i-1][1]).days
        consecutive_diffs.append(diff)
    return consecutive_diffs

if __name__ == "__main__":
    print(get_consecutive_diffs())
