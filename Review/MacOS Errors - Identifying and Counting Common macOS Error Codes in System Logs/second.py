from first import get_log_text
import re

error_codes_list = [-67062, 22, 113]
log_text = get_log_text()
for code in error_codes_list:
    pattern = re.compile(rf"(?<!\d){re.escape(str(code))}(?!\d)")
    count = len(pattern.findall(log_text))
    print(code, count)
