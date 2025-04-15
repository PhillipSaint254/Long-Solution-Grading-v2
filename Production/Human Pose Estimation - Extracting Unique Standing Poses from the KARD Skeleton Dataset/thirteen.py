import pandas as pd, numpy as np
from twelve import get_joint_names
from nine import get_unique_frames

def get_pose_rows():
    pose_rows = []
    unique_frames = get_unique_frames()
    joint_names = get_joint_names()
    for pose_id, (key, frame) in enumerate(unique_frames.items(), start=1):
        for joint_idx, joint_name in enumerate(joint_names):
            x, y, z = frame[joint_idx]
            coord_str = f"({x:.1f}, {y:.1f}, {z:.1f})"
            pose_rows.append({"Pose ID": pose_id, "Key Point": joint_name, "Coordinates": coord_str})
    return pose_rows
        
def get_df_poses():
    pose_rows = get_pose_rows()
    return pd.DataFrame(pose_rows)

if __name__ == "__main__":
    df_poses = get_df_poses()
    print(df_poses.head())
