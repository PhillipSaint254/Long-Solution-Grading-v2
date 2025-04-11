
def get_ratings():
     return [4.5, 4.0, 4.2, 4.0, 4.5, 4.9, 4.2, 4.3, 4.7, 4.3]

def get_avg_rating():
    ratings = get_ratings()
    return sum(ratings)/len(ratings)

if __name__ == "__main__":
    print(get_ratings())
