from _six import get_doc2_sections
from collections import Counter
import re

doc2_sections = get_doc2_sections()

all_items_text2 = ' '.join(sum(doc2_sections.values(), []))
words2 = re.findall(r"[A-Za-z'-]+", all_items_text2.lower())
freq2 = Counter(words2)
print(freq2.most_common(20))
