import pandas as pd

def get_restaurant_data():
    return [
        {"Restaurant": "La Parisienne", "Rating": 4.6, "Reviews": 1000},
        {"Restaurant": "The Malt House", "Rating": 4.0, "Reviews": 533},
        {"Restaurant": "Liberty Bagels", "Rating": 4.2, "Reviews": 425},
        {"Restaurant": "Toro Loco", "Rating": 4.0, "Reviews": 513},
        {"Restaurant": "Pisillo Italian Panini", "Rating": 4.5, "Reviews": 22},
        {"Restaurant": "Regular NYC", "Rating": 4.9, "Reviews": 52},
        {"Restaurant": "Hole In The Wall - FiDi", "Rating": 4.2, "Reviews": 854},
        {"Restaurant": "Hey Thai", "Rating": 4.3, "Reviews": 247},
        {"Restaurant": "Mikado", "Rating": 4.7, "Reviews": 185},
        {"Restaurant": "Westville", "Rating": 4.3, "Reviews": 324}
    ]

def get_df_avg_rating():
    restaurant_data = get_restaurant_data()
    df = pd.DataFrame(restaurant_data)
    avg_rating = round(df["Rating"].mean(), 2)
    df["Comparison"] = df["Rating"].apply(lambda x: "Above Avg" if x>avg_rating else ("Equal to Avg" if x==avg_rating else "Below Avg"))
    return df, avg_rating

if __name__ == "__main__":
    df, avg_rating = get_df_avg_rating()
    print(avg_rating)
    print(df)
