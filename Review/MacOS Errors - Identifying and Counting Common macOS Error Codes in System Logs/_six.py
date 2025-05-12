from first import get_log_text

log_text = get_log_text()
for i, line in enumerate(log_text.splitlines(), start=1):
    if "[22:" in line:
        print(i, line[:80])
