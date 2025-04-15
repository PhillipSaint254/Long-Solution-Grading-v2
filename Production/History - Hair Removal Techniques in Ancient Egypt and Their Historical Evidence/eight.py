from _six import extract_years
from five import get_sources_text

sources_text = get_sources_text()
print(extract_years(sources_text["curationist"])[:20])
print(sources_text["curationist"])
