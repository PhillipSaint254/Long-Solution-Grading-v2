from nine import get_unique_frames

def get_first_key_frame():
    unique_frames = get_unique_frames()
    unique_frames_indexed = list(unique_frames.items())
    return unique_frames_indexed[0]

if __name__ == "__main__":
    _, first_frame = get_first_key_frame()
    print(first_frame)
