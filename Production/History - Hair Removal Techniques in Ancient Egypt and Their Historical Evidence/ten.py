from nine import get_sources_text
from _six import collect_years, count_references
from seven import get_methods_keywords

sources_text = get_sources_text()
methods_keywords = get_methods_keywords()

method_counts_source = count_references(sources_text, methods_keywords)
method_years = collect_years(sources_text, methods_keywords)
print(method_counts_source, method_years)
