from five import get_measures

def get_standing_frames_indices():
    measures = get_measures()
    standing_threshold = 1420
    return [i for i, m in enumerate(measures) if m > standing_threshold]

if __name__ == "__main__":
    standing_frames_indices = get_standing_frames_indices()
    print(len(standing_frames_indices), standing_frames_indices[:10])
