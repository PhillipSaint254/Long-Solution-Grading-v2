import numpy as np
from four import get_frames

def standing_measure(frame):
    # frame is list of 15 [x,y,z]
    # compute vertical height difference (assuming y dimension vertical)
    y_head = frame[0][1]
    y_right_foot = frame[11][1]
    y_left_foot = frame[14][1]
    y_feet_mean = (y_right_foot + y_left_foot) / 2.0
    return abs(y_head - y_feet_mean)

# compute measure for each frame
def get_measures():
    frames = get_frames()
    return [standing_measure(frame) for frame in frames]

if __name__ == "__main__":
    measures = get_measures()
    print(max(measures), min(measures))
