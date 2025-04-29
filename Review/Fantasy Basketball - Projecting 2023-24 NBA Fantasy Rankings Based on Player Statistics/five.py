from four import get_player_agg

def get_top100():
    player_agg = get_player_agg()
    return player_agg.sort_values(by='FantasyPoints', ascending=False).head(100)

if __name__ == "__main__":
    print(len(get_top100()), get_top100().head())
