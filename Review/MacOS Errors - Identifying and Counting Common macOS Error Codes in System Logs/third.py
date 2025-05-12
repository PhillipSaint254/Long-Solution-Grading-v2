from first import get_log_text
import re 

log_text = get_log_text()
pattern = re.compile(r'(?:Code=|#-|\[)(-?\d+)')
matches = pattern.findall(log_text)
print(matches[:10], len(matches))
