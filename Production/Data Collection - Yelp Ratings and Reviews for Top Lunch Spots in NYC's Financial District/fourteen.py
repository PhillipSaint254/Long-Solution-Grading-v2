from thirteen import get_ratings, get_avg_rating

def get_comparisons():
    ratings = get_ratings()
    avg_rating = get_avg_rating()
    return ['above' if r>avg_rating else ('below' if r<avg_rating else 'equal') for r in ratings]

if __name__ == "__main__":
    comparisons = get_comparisons()
    print(comparisons)
