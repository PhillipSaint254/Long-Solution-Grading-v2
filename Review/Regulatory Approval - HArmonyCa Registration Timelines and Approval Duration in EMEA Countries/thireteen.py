from twelf import get_diffs
import statistics

def get_avg_diff_excl_earliest():
    diffs = get_diffs()
    return statistics.mean([d for d in diffs.values() if d>0])

if __name__ == "__main__":
    print(get_avg_diff_excl_earliest())
