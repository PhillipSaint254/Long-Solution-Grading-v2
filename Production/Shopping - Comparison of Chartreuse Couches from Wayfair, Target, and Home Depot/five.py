from second import get_couch_data

def get_highest_rating():
    couch_data = get_couch_data()    
    return max(couch_data, key=lambda x: x["Rating"])

if __name__ == "__main__":
    highest_rating = get_highest_rating()
    print(highest_rating)
    