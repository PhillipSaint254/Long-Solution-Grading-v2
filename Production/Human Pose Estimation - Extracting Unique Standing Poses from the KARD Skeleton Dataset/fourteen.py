from eight import get_standing_frames_indices
from five import get_measures

def get_standing_measures_selected():
    measures = get_measures()
    standing_frames_indices = get_standing_frames_indices()
    return [measures[i] for i in standing_frames_indices]


if __name__ == "__main__":
    standing_measures_selected = get_standing_measures_selected()
    print(standing_measures_selected[:10], min(standing_measures_selected), max(standing_measures_selected))
