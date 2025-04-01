from four import get_array
import numpy as np

arr = get_array()

# Compute full decile boundaries
percentiles = np.percentile(arr, np.arange(0, 110, 10))  # 0, 10, 20, ..., 100
print(percentiles)
