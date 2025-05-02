from first import get_differences
import numpy as np, statistics

differences = get_differences()
avg_days = statistics.mean(differences)
print(avg_days)
