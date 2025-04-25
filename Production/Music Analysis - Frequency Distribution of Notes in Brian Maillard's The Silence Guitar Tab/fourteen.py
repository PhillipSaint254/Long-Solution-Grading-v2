from thirteen import get_boxes_str, parse_boxes

def get_cluster_means():
    df_boxes = parse_boxes(get_boxes_str())
    return df_boxes.groupby('string_cluster')['center_y'].mean()

if __name__ == "__main__":
    cluster_means = get_cluster_means()
    print(cluster_means)
