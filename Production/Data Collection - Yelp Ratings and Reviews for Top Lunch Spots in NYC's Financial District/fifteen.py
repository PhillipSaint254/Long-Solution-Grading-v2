import pandas as pd

def get_restaurant_data():
    return [
        ("La Parisienne", 4.6, 1000),
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

def get_df_avg_rating():
    restaurant_data = get_restaurant_data()
    df = pd.DataFrame(restaurant_data, columns=["Restaurant", "Rating", "Reviews"])
    avg_rating = round(df["Rating"].mean(), 2)
    df["Comparison"] = df["Rating"].apply(lambda x: "Above Avg" if x>avg_rating else ("Equal to Avg" if x==avg_rating else "Below Avg"))
    return df, avg_rating


if __name__ == "__main__":
    df, avg_rating = get_df_avg_rating()
    print(df, avg_rating)
