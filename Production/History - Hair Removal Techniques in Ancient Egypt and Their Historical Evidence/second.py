from first import get_sources_text

# methods and keywords
def get_methods_keywords():
    return {
    "Razor/Shaving": ["razor", "shaving", "shaved"], # we also have 'shave' etc; but we will use base 'shav'
    "Tweezers": ["tweezer", "tweezers"],
    "Pumice Stone": ["pumice"],
    "Wax/Sugaring": ["beeswax", "sugar", "wax"],
    "Depilatory Cream/Potions": ["depilatory", "potion", "paste"],
    }

# count occurrences
def get_method_counts():
    sources_text = get_sources_text()
    methods_keywords = get_methods_keywords()
    method_counts = {method: 0 for method in methods_keywords}
    for name, text in sources_text.items():
        text_lower = text.lower()
        for method, keywords in methods_keywords.items():
            for kw in keywords:
                if kw in text_lower:
                    method_counts[method] += text_lower.count(kw)
    return method_counts

if __name__ == "__main__":
    method_counts = get_method_counts()
    print(method_counts)
