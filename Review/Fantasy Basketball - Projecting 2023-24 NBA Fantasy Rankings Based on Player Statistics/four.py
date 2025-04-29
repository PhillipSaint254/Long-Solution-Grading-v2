from third import get_player_agg as gpa1

def get_player_agg():
    # compute fantasy points per game
    player_agg = gpa1()
    player_agg['FantasyPoints'] = 1*player_agg['PPG'] + 1.2*player_agg['RPG'] + 1.5*player_agg['APG'] + 3*player_agg['SPG'] + 3*player_agg['BPG']
    return player_agg

if __name__ == "__main__":
    player_agg = get_player_agg()
    print(player_agg.sort_values(by='FantasyPoints', ascending=False).head())
