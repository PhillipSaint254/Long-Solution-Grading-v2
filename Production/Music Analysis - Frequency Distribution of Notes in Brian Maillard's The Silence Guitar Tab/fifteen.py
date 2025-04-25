from fourteen import get_cluster_means

def get_order():
    cluster_means = get_cluster_means()
    return cluster_means.sort_values(ascending=False).index.tolist()

if __name__ == "__main__":
    order = get_order()
    print(order)
