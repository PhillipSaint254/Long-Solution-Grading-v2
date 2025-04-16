# Setup data
def get_countries_data():
    countries_data = {
        "United States": {
            "salary_monthly_usd": 4334.64,
            "house_usd": 265738,
            "food_usd": 504,
            "phone_usd": 999,
            "car_usd": 27110
        },
        "Germany": {
            "salary_monthly_usd": 3076.48,
            "house_usd": 232140,  # 219000 * 1.06
            "food_usd": 265,  # 250*1.06
            "phone_usd": 1270,  # 1199*1.06
            "car_usd": 18959  # 17900*1.06 (approx)
        },
        "India": {
            "salary_monthly_usd": 537.30,
            "house_usd": 73096.13,
            "food_usd": 88.88,
            "phone_usd": 1612.06,
            "car_usd": 9560
        },
        "South Africa": {
            "salary_monthly_usd": 1282.48,
            "house_usd": 46367.01,
            "food_usd": 122.74,
            "phone_usd": 1058.2,
            "car_usd": 20390.57
        },
        "United Kingdom": {
            "salary_monthly_usd": 3050.64,
            "house_usd": 217277.0,
            "food_usd": 214.72,
            "phone_usd": 1276.82,
            "car_usd": 27440.81
        }
    }

    for country, data in countries_data.items():
        total_cost = data["house_usd"] + data["food_usd"] + data["phone_usd"] + data["car_usd"]
        months = total_cost / data["salary_monthly_usd"]
        data["total_cost"] = total_cost
        data["months_to_afford"] = months

    return countries_data

if __name__ == "__main__":
    countries_data = get_countries_data()
    print(countries_data)
