# Let's compute totals and averages for the years 2019-2023 with article counts = 0

years = list(range(2019, 2024))
counts = [0] * len(years)
total = sum(counts)
average = total / len(years)  # float
print(years, counts, total, average)
