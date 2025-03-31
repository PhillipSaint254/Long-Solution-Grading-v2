import pandas as pd
from _twenty import get_europe_data

def get_df():
    europe_data = get_europe_data()

    # Create DataFrame
    return pd.DataFrame(europe_data, columns=['Country','Population','OphPerMillion','Total','EnteringPractice','LeavingPractice','PctDoingSurgery','Residents','Updated'])

def get_df_sorted():
    df = get_df()
    # Keep only necessary columns and convert numbers
    df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

    # Compute per 100k
    df['Oph_per_100k'] = df['Total'] / df['Population'] * 100000

    # Sort
    return df.sort_values('Oph_per_100k', ascending=False)

if __name__ == "__main__":
    df_sorted = get_df_sorted()
    print(df_sorted[['Country','Total','Population','Oph_per_100k']].head(10))
