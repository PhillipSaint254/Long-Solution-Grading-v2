# Let's construct the dataset
import numpy as np

def get_groups():
    # define groups
    return [
        {"range": (300, 579), "pct": 12.6},
        {"range": (580, 669), "pct": 15.8},
        {"range": (670, 739), "pct": 21.6},
        {"range": (740, 799), "pct": 28.1},
        {"range": (800, 850), "pct": 21.9},
    ]

def get_scores():
    groups = get_groups()
    
    # total percentages sum check
    total_pct = sum(g['pct'] for g in groups)
    print(total_pct)

    # choose sample size:
    N = 100000

    # build the data
    scores = []
    for g in groups:
        lo, hi = g['range']
        midpoint = (lo + hi) / 2.0
        count = int(round(g['pct'] / 100 * N))
        scores.extend([midpoint] * count)
    return scores

if __name__ == "__main__":
    # ensure total length:
    scores = get_scores()
    print(len(scores), scores[:10], scores[-10:])
