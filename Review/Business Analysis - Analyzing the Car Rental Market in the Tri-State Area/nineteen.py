from seventeen import get_location_data
from eighteen import get_pricing, get_ratings
import pandas as pd

def get_data():
    data = []
    location_data = get_location_data()
    pricing = get_pricing()
    ratings = get_ratings()
    for state in ["New York", "New Jersey", "Connecticut"]:
        data.append({
            "State": state,
            "Enterprise Locations": location_data[state],
            "Average Rental Price (per day, Kayak)": f"${pricing[state]}",
            "Top Rated Company (Kayak) & Rating": f"{ratings[state]['Top Company']} ({ratings[state]['Rating']})"
        })
    return data

def get_df():
    data = get_data()
    return pd.DataFrame(data)

if __name__ == "__main__":
    print(get_df())
