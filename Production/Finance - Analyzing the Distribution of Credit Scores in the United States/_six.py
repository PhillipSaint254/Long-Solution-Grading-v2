import numpy as np
from third import get_groups

# Let's generate random scores uniformly within each group
np.random.seed(0)  # for reproducibility

def get_arr_rand():
    groups = get_groups()
    N = 100000

    scores_rand = []
    for g in groups:
        lo, hi = g['range']
        count = int(round(g['pct'] / 100 * N))
        # sample uniformly in [lo, hi], inclusive
        sample = np.random.uniform(lo, hi, size=count)
        scores_rand.append(sample)

    return np.concatenate(scores_rand)

def get_arr_mean():
    arr_rand = get_arr_rand()
    return arr_rand.mean()

def get_arr_median():
    arr_rand = get_arr_rand()
    return np.median(arr_rand)

def get_arr_std():
    arr_rand = get_arr_rand()
    return arr_rand.std(ddof=0)

if __name__ == "__main__":
    mean_rand = get_arr_mean()
    median_rand = get_arr_median()
    std_rand = get_arr_std()
    arr_rand = get_arr_rand()
    deciles_rand = np.percentile(arr_rand, np.arange(10, 100, 10))
    print("Mean:", mean_rand, "Median:", median_rand, "Std:", std_rand)
    print("Deciles:", deciles_rand)

    # check percentages within deciles
    bins = np.percentile(arr_rand, np.arange(0, 110, 10))
    counts = np.histogram(arr_rand, bins=bins)[0]
    percentages_dec = counts / len(arr_rand) * 100

    print(percentages_dec)
