# Let's aggregate all the items from doc1 and compute word frequencies.

from collections import Counter
import re
from four import get_doc1_sections

doc1_sections = get_doc1_sections()

all_items_text1 = ' '.join(sum(doc1_sections.values(), []))  # flatten list
# Lowercase and split words (keeping only alphabetic)
words1 = re.findall(r"[A-Za-z'-]+", all_items_text1.lower())
freq1 = Counter(words1)
print(freq1.most_common(20))
