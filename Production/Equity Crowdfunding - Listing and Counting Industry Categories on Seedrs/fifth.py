from fourth import get_categories

def get_unique_categories():
    categories = get_categories()
    return sorted(set(categories))

if __name__ == "__main__":
    unique_categories = get_categories()
    print(unique_categories, len(unique_categories))
