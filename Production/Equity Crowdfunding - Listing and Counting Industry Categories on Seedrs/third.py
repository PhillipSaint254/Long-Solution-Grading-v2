from first import get_categories

categories = get_categories()
print(len(set([c.strip() for c in categories])))
