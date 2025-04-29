from five import get_top100 as gt100

def get_top100_reset():
    top100 = gt100()
    return top100.reset_index().rename(columns={'NAME':'Player'})


if __name__ == "__main__":
    top100_reset = get_top100_reset()
    top100_reset.insert(0, 'Rank', range(1, len(top100_reset)+1))
    print(top100_reset.head())
