import numpy as np, pandas as pd
from eight import get_standing_frames_indices, get_frames

def frame_to_tuple(frame, decimals=1):
    arr = np.round(frame, decimals=decimals)  # rounding for uniqueness
    return tuple(arr.flatten())

# create dictionary to store unique poses
def get_unique_frames():
    standing_frames_indices = get_standing_frames_indices()
    frames = get_frames()
    unique_frames = {}
    for idx in standing_frames_indices:
        frame = np.array(frames[idx])
        key = frame_to_tuple(frame, decimals=1)
        if key not in unique_frames:
            unique_frames[key] = frame
    return unique_frames

if __name__ == "__main__":
    unique_frames = get_unique_frames()
    print(len(unique_frames))
