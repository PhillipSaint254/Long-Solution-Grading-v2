from eight import get_avg_rating, get_ratings

ratings = get_ratings()
avg_rating = get_avg_rating()
comparisons = ['above' if r>avg_rating else 'equal' if r==avg_rating else 'below' for r in ratings]
print(comparisons)
