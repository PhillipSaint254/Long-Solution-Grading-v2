from dataframe import get_df as gdf

def get_df():
    df_sorted = get_df()
    df_sorted['months_to_afford_years'] = df_sorted['months_to_afford'] / 12
    df_sorted[['salary_monthly_usd','total_cost','months_to_afford','months_to_afford_years']]
    return df_sorted
