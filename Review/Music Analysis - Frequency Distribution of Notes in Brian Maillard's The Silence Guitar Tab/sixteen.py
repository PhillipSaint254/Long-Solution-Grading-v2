from thirteen import get_cluster_means

def get_top_clusters():
    cluster_means = get_cluster_means()
    return cluster_means.sort_values(ascending=False).index.tolist()

def get_string_map():
    top_clusters = get_top_clusters()
    return {cluster: i+1 for i, cluster in enumerate(top_clusters)}

if __name__ == "__main__":
    print(get_string_map())
    