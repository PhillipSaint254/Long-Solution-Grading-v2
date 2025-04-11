
def get_shoes():
    return {
        "North Face Chilkat V 400": {"warmth":8.0, "waterproof":8.0, "traction":9.0, "price":158},
        "Columbia Bugaboot III": {"warmth":7.5, "waterproof":8.0, "traction":8.5, "price":66},
        "Baffin Chloe": {"warmth":10.0, "waterproof":9.5, "traction":8.5, "price":97},
        "UGG Adirondack III": {"warmth":9.0, "waterproof":8.0, "traction":7.0, "price":250},
        "Icebug NewRun BUGrip GTX": {"warmth":5.0, "waterproof":9.0, "traction":10.0, "price":230}  # approximate for Runner's world
    }

if __name__ == "__main__":
    shoes = get_shoes()
    print(shoes)
