def get_game_hands_per_hour():
    return {
        'Blackjack': 120, # we have 30 sec per round -> 120 per hour (assuming 120 for average from earlier? Wait 30 sec per 4-player - 120 hands/h. We'll confirm though - yes 30 sec -> 120)
        'Baccarat': 120, # from 120 easy per hour
        'Casino War': 65,
        'Caribbean Stud Poker': 50,
        'Let It Ride': 52
    }

if __name__ == "__main__":
    game_hands_per_hour = get_game_hands_per_hour()
    game_durations_minutes = {game: round(60 / hph, 2) for game, hph in game_hands_per_hour.items()}
    print(game_durations_minutes)
