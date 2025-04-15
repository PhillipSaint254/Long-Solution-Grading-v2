from third import get_triplets

def get_frames():
    num_joints = 15
    triplets = get_triplets()
    return [triplets[i:i+num_joints] for i in range(0, len(triplets), num_joints)]

if __name__ == "__main__":
    frames = get_frames()
    print(len(frames))
