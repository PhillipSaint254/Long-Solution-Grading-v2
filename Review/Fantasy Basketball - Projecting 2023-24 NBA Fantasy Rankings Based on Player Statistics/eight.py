from _six import get_top100_reset

def get_top100_reset_rounded():
    top100_reset = get_top100_reset()
    return top100_reset.round({'PPG':1, 'RPG':1, 'APG':1, 'SPG':1, 'BPG':1, 'MPG':1, 'FantasyPoints':2})

if __name__ == "__main__":
    print(len(get_top100_reset_rounded().to_markdown()))
