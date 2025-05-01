from collections import Counter
from first import get_events

def get_counter():
    events = get_events()
    return Counter([e["disease_or_contaminant"] for e in events])

if __name__ == "__main__":
    print(get_counter())
