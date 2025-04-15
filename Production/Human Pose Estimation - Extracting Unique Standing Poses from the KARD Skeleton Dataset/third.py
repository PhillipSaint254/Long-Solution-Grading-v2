from second import get_text_lines

def get_triplets():
    text_lines = get_text_lines()
    # parse lines into lists of 3 floats
    return [list(map(float, line.strip().split())) for line in text_lines]


if __name__ == "__main__":
    triplets = get_triplets()
    print(triplets[:5], len(triplets))
