from _six import get_diffs
import statistics

def get_avg_all():
    diffs = get_diffs()
    return statistics.mean(diffs.values())

if __name__ == "__main__":
    print(get_avg_all())
