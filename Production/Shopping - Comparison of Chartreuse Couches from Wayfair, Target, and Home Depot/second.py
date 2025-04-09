
def get_couch_data():
    return [
        {"Retailer": "Target", "Couch": "Best Choice Products Modern Linen Convertible Futon Sofa Bed - Chartreuse", "Price": 139.99, "Rating": 3.6},
        {"Retailer": "Wayfair", "Couch": "Hasaam 56.3\" Wide Velvet Round Arms Loveseat - Chartreuse", "Price": 249.99, "Rating": 4.5},
        {"Retailer": "Home Depot", "Couch": "63 in. Square Arm Fabric Upholstered Sofa - Chartreuse", "Price": 1349.00, "Rating": 4.5}
    ]

def get_sorted_couches():
    couch_data = get_couch_data()
    return sorted(couch_data, key=lambda x: x["Price"])

if __name__ == "__main__":
    sorted_couches = get_sorted_couches()
    print(sorted_couches)
    