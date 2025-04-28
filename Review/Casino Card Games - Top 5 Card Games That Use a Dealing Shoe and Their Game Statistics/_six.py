from third import get_avg_cards
from four import get_durations

def get_avg_duration_rounded():
    avg_cards = get_avg_cards()
    durations = get_durations()
    avg_cards_rounded = {k: round(v, 2) for k, v in avg_cards.items()}
    durations_rounded = {k: round(v, 2) for k, v in durations.items()}
    return avg_cards_rounded, durations_rounded

if __name__ == "__main__":
    avg_cards_rounded, durations_rounded = get_avg_duration_rounded()
    print(avg_cards_rounded, durations_rounded)
    