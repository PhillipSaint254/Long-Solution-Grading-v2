from ten import parse_boxes, get_boxes_str

def get_df_boxes():
    return parse_boxes(get_boxes_str())

def get_cluster_means():
    df_boxes = get_df_boxes()
    return df_boxes.groupby('string_cluster')['center_y'].mean()

if __name__ == "__main__":
    cluster_means = get_cluster_means()
    print(cluster_means)
    