from eleven import get_avg_rating, get_ratings

def get_comparisons():
    avg_rating = get_avg_rating()
    ratings = get_ratings()
    return ['above' if r>avg_rating else 'equal' if r==avg_rating else 'below' for r in ratings]

if __name__ == "__main__":
    comparisons = get_comparisons()
    print(list(zip([ "La Parisienne","The Malt House","Liberty Bagels","Toro Loco","Pisillo Italian Panini","Regular NYC","Hole In The Wall - FiDi", "Hey Thai","Mikado","Westville"], comparisons)))
