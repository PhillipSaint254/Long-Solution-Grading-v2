import numpy as np
from five import get_measures

def get_quantiles():
    measures = get_measures()
    return np.quantile(measures, [0.25, 0.5, 0.75, 0.9, 0.95])

if __name__ == "__main__":
    quantiles = get_quantiles()
    print(quantiles)
