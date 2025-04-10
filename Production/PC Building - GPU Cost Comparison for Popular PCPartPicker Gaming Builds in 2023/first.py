
def get_builds():
    builds = {
        "Great AMD Gaming Build": {"gpu_price": 399.99, "total_price": 1087.80},
        "Great Intel Gaming Build": {"gpu_price": 329.99, "total_price": 1006.55},
        "Magnificent AMD Gaming/Streaming Build": {"gpu_price": 794.99, "total_price": 1895.91},
        "Enthusiast AMD Gaming/Streaming Build": {"gpu_price": 769.99, "total_price": 1598.89},
        "Glorious/Excellent Intel Gaming/Streaming Build": {"gpu_price": 1599.00, "total_price": 2978.56},
    }

    for name, data in builds.items():
        data["gpu_percentage"] = data["gpu_price"] / data["total_price"] * 100
    return builds

if __name__ == "__main__":
    builds = get_builds()
    print(builds)
