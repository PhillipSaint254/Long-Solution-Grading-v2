import statistics
from four import get_consecutive_diffs

consecutive_diffs = get_consecutive_diffs()
avg_consecutive = statistics.mean(consecutive_diffs)
print(avg_consecutive)
