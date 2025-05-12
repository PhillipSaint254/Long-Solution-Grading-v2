from first import get_log_text
import re

def get_matches_code():
    log_text = get_log_text()
    pattern_code = re.compile(r'Code=(-?\d+)')
    return pattern_code.findall(log_text)

def get_matches_bracket():
    log_text = get_log_text()
    pattern_bracket = re.compile(r'\[(-?\d+):')
    return pattern_bracket.findall(log_text)

if __name__ == "__main__":
    matches_code = get_matches_code()
    matches_bracket = get_matches_bracket()
    print(matches_code, matches_bracket[:10])
