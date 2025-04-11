import pandas as pd
import numpy as np

def get_restaurant_data():
    return [
        ("La Parisienne", 4.5, 1039),
        ("The Malt House", 4.0, 533),
        ("Liberty Bagels", 4.2, 425),
        ("Toro Loco", 4.0, 513),
        ("Pisillo Italian Panini", 4.5, 22),
        ("Regular NYC", 4.9, 52),
        ("Hole In The Wall - FiDi", 4.2, 854),
        ("Hey Thai", 4.3, 247),
        ("Mikado", 4.7, 185),
        ("Westville", 4.3, 324)
    ]

def get_base_df():
    """Returns the raw DataFrame without any extra columns."""
    data = get_restaurant_data()
    return pd.DataFrame(data, columns=["Restaurant", "Rating", "Reviews"])

def get_df_with_comparison():
    """Returns DataFrame with a column comparing each rating to the average."""
    df = get_base_df()
    avg_rating = round(df["Rating"].mean(), 2)
    df["Comparison to Avg"] = df["Rating"].apply(
        lambda x: "above" if x > avg_rating else ("below" if x < avg_rating else "equal")
    )
    return df

if __name__ == "__main__":
    df = get_df_with_comparison()
    print("Restaurant Ratings Compared to Average:\n")
    print(df)
