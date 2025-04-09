
def get_prices():
    return {
        'Wayfair Hasaam Loveseat': 249.99,
        'Target Futon Sofa Bed': 139.99,
        'Home Depot Square Arm Sofa': 1349.00
    }

def get_sorted_prices():
    prices = get_prices()
    return sorted(prices.items(), key=lambda x: x[1])

if __name__ == "__main__":
    sorted_prices = get_sorted_prices()
    print(sorted_prices)
