import pandas as pd
from third import get_scores
import numpy as np

def get_array():
    scores = get_scores()

    return np.array(scores)

if __name__ == "__main__":
    arr = get_array()
    mean = arr.mean()
    median = np.median(arr)
    std = arr.std(ddof=0)  # population std
    print("Mean:", mean, "Median:", median, "Std:", std)

    # deciles
    deciles = np.percentile(arr, [10,20,30,40,50,60,70,80,90])

    print(deciles)
