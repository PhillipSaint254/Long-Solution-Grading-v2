from thirteen import get_df_poses

df_poses = get_df_poses()
df_first5 = df_poses[df_poses["Pose ID"] <= 5]
print(df_first5.tail())
