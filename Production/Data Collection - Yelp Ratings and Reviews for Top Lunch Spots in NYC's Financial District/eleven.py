
def get_ratings():
    return [4.6, 4.0, 4.2, 4.0, 4.5, 4.9, 4.2, 4.3, 4.7, 4.3]

def get_avg_rating():
    ratings = get_ratings()
    return round(sum(ratings)/len(ratings),2)

if __name__ == "__main__":
    print(get_avg_rating())
