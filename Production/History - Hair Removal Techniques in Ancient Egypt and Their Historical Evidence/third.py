from first import get_sources_text
from second import get_methods_keywords

def get_method_counts_source():
    sources_text = get_sources_text()
    methods_keywords = get_methods_keywords()
    method_counts_source = {method:0 for method in methods_keywords}
    for text in sources_text.values():
        text_lower = text.lower()
        for method, keywords in methods_keywords.items():
            # if any of the keywords appear
            if any(kw in text_lower for kw in keywords):
                method_counts_source[method]+=1
    return method_counts_source

if __name__ == "__main__":
    print(get_method_counts_source())
