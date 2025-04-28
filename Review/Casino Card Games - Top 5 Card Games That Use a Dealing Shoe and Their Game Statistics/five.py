from four import get_durations
from third import get_avg_cards

def get_avg_cards_rounded():
    avg_cards = get_avg_cards()
    return {game: round(cards, 2) for game, cards in avg_cards.items()}

if __name__ == "__main__":
    avg_cards_rounded = get_avg_cards_rounded()
    durations_rounded = get_durations()
    print(avg_cards_rounded, durations_rounded)
