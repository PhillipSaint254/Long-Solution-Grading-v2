import re
from second import get_methods_keywords
from five import get_sources_text

def count_references(texts, methods_keywords):
    counts = {method: 0 for method in methods_keywords}
    for text in texts.values():
        text_lower = text.lower()
        for method, keywords in methods_keywords.items():
            if any(kw in text_lower for kw in keywords):
                counts[method] += 1
    return counts

def extract_years(text):
    years = re.findall(r'(\d{3,4})\s*b\.?c', text.lower())
    return [int(y) for y in years]

def collect_years(texts, methods_keywords):
    method_years = {m: [] for m in methods_keywords}
    for text in texts.values():
        years = extract_years(text)
        for method, keywords in methods_keywords.items():
            if any(kw.lower() in text.lower() for kw in keywords):
                method_years[method].extend(years)
    return method_years

if __name__ == "__main__":
    sources_text = get_sources_text()
    methods_keywords = get_methods_keywords()
    method_counts_source = count_references(sources_text, methods_keywords)
    method_years = collect_years(sources_text, methods_keywords)
    print(method_counts_source, method_years)
