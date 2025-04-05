from collections import Counter
from eight import get_doc3_sections
import re

doc3_sections = get_doc3_sections()

all_items_text3 = ' '.join(sum(doc3_sections.values(), []))
words3 = re.findall(r"[A-Za-z0-9'-]+", all_items_text3.lower())
freq3 = Counter(words3)
print(freq3.most_common(30))
