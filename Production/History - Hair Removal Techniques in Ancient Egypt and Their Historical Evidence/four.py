from first import get_sources_text
from second import get_methods_keywords
import re, numpy as np, pandas as pd, math

def extract_years(text):
    # regex to capture digits 1000-4000 etc
    years = re.findall(r'(\d{3,4})\s*B\.?C', text)
    return [int(y) for y in years]

# create mapping of method to all year numbers from sources that mention the method
def get_method_years():
    sources_text = get_sources_text()
    methods_keywords = get_methods_keywords()
    method_years = {method: [] for method in methods_keywords}
    for text in sources_text.values():
        text_lower = text.lower()
        years = extract_years(text)
        for method, keywords in methods_keywords.items():
            if any(kw in text_lower for kw in keywords):
                method_years[method].extend(years)
    return method_years

if __name__ == "__main__":
    print(get_method_years())
