from first import get_differences
import numpy as np, statistics

def get_avg_days():
    differences = get_differences()
    return statistics.mean(differences)

if __name__ == "__main__":
    print(get_avg_days())
