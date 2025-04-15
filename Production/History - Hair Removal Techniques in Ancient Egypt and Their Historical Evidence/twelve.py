from _six import collect_years, count_references
from eleven import get_sources_text
from seven import get_methods_keywords

sources_text = get_sources_text()
methods_keywords = get_methods_keywords()

def get_method_counts_source():
    return count_references(sources_text, methods_keywords)

def get_method_years():
    return collect_years(sources_text, methods_keywords)

if __name__ == "__main__":
    method_counts_source = get_method_counts_source()
    method_years = get_method_years()
    print(method_counts_source, method_years)
