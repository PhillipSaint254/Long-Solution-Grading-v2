from five import get_df

# average monthly spending per year for dataset of 100 users (i.e., across months)
# For each year, compute mean of monthly averages (not per user)
def get_yearly_avg_monthly():
    df = get_df()
    
    # Add year column to df
    df['year'] = df['date'].dt.year
    return df.groupby(['year', 'date'])['spend'].mean().groupby('year').mean()


if __name__ == "__main__":
    yearly_avg_monthly = get_yearly_avg_monthly()
    print(yearly_avg_monthly)
