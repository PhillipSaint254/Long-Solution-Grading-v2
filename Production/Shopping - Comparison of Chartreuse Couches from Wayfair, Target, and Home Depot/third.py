from second import get_couch_data

# Determine highest rating (select by rating then number of reviews)
def get_sorted_by_rating():
    couch_data = get_couch_data()
    return sorted(couch_data, key=lambda x: (-x["Rating"], x["Price"]))  # high rating first; if tie, choose cheaper maybe.

if __name__ == "__main__":
    sorted_by_rating = get_sorted_by_rating()
    print(sorted_by_rating)
