from seven import get_seasonal

# Using seasonal component from decomposition; we only need first 12 months to capture repeating pattern
# We'll take first 12 months from decomposition (2020 months) to represent pattern
def get_seasonal_pattern():
    seasonal = get_seasonal()
    return seasonal[:12]

if __name__ == "__main__":
    seasonal_pattern = get_seasonal_pattern()
    print(seasonal_pattern)
