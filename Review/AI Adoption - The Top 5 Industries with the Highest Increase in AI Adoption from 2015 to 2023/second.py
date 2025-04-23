from first import get_increases

def get_sorted_increases():
    increases = get_increases()
    return sorted(increases.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    sorted_increases = get_sorted_increases()
    print(sorted_increases)
