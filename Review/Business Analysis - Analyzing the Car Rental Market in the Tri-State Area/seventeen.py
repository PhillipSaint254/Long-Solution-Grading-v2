from nine import get_location_count

def get_location_data():
    ny_total, _ = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/ny.html")
    nj_total, _ = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/nj.html")
    ct_total, _ = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/ct.html")
    return {
        "New York": ny_total,
        "New Jersey": nj_total,
        "Connecticut": ct_total
    }

if __name__ == "__main__":
    print(get_location_data())
