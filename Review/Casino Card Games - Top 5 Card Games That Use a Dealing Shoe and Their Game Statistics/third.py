def get_avg_cards():
    return {
        'Blackjack': 2.71 + 2.78,  # from lines
        'Baccarat': 2.503332474 + 2.435277628,
        'Casino War': 2*(1 - 23/311) + 10*(23/311), # probability tie 23/311; using 10 cards if tie (2 initial + 6 burn + 2 war)
        'Caribbean Stud Poker': 5*2,  # 5 to each player and dealer
        'Let It Ride': 3 + 2 # 3 to player + 2 community
    }

if __name__ == "__main__":
    avg_cards = get_avg_cards()
    print(avg_cards)
