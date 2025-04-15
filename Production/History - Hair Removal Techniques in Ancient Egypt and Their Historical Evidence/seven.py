from _six import count_references, collect_years
from five import get_sources_text

# adjust keywords
def get_methods_keywords():
    return {
    "Razor/Shaving": ["razor", "shav"], # capturing shav (shave, shaved, shaving)
    "Tweezers": ["tweezer", "seashells"], # to capture 'tweezing with seashells'
    "Pumice Stone": ["pumice"],
    "Wax/Sugaring": ["beeswax", "sugar", "wax"], 
    "Depilatory Cream/Potions": ["depilatory", "potion", "paste"],
    }

if __name__ == "__main__":
    sources_text = get_sources_text()
    methods_keywords = get_methods_keywords()
    method_counts_source = count_references(sources_text, methods_keywords)
    method_years = collect_years(sources_text, methods_keywords)
    print(method_counts_source, method_years)
