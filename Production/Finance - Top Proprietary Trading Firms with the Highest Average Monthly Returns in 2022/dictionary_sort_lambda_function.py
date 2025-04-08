# We have the 2022 total rates of return (annual) for five firms (measured as sum of monthly returns).

# Values (as percentages):

ror_data = {
    "DUNN Capital Management — WMA": 60.24,  # gleaned from source [52]
    "Winoma Capital — FX Growth": 24.84,    # gleaned from [43]
    "AIS Capital Management — MAAP (2X–4X)": 21.19,  # gleaned from [40]
    "Opus Futures, LLC — Advanced Ag": 8.95, # gleaned from [46]
    "Red Rock Capital — Commodity L/S": 8.73 # gleaned from [49]
}

# Compute average monthly return = total / 12

avg_monthly = {name: ror / 12.0 for name, ror in ror_data.items()}

# Create a sorted list by average descending.

sorted_avg = sorted(avg_monthly.items(), key=lambda x: x[1], reverse=True)

print(sorted_avg)
