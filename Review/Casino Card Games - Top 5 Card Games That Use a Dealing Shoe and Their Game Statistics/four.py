
def get_durations():
    return {
        'Blackjack': 0.5, # 30 sec per round (0.5 min)
        'Baccarat': 60/120, # 120 hands per hour -> 0.5
        'Casino War': round(60/65, 2),
        'Caribbean Stud Poker': round(60/50, 2),
        'Let It Ride': round(60/52, 2)
    }

if __name__ == "__main__":
    durations = get_durations()
    print(durations)
