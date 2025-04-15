def get_joint_names():
    return ["Head", "Neck", "Right Shoulder", "Right Elbow", "Right Hand",
               "Left Shoulder", "Left Elbow", "Left Hand", "Torso",
               "Right Hip", "Right Knee", "Right Foot", "Left Hip", "Left Knee", "Left Foot"]


if __name__ == "__main__":
    joint_names = get_joint_names()
    print(len(joint_names))
