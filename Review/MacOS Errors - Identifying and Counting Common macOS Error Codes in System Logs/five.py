from four import get_matches_bracket, get_matches_code

matches_code = get_matches_code()
matches_bracket = get_matches_bracket()

# convert to integers
codes = [int(x) for x in matches_code + matches_bracket]
from collections import Counter
print(Counter(codes))
