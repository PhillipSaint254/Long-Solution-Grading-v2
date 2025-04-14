from five import get_df

# Compute month-of-year averages
def get_monthly_means():
    df = get_df()
    df['month'] = df['date'].dt.month
    return df.groupby('month')['spend'].mean()

if __name__ == "__main__":
    monthly_means = get_monthly_means()
    print(monthly_means)
