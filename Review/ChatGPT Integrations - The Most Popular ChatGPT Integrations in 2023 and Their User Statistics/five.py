import pandas as pd
from four import get_rows

def get_sorted_rows():
    rows = get_rows()
    return sorted(rows, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print(get_sorted_rows())
