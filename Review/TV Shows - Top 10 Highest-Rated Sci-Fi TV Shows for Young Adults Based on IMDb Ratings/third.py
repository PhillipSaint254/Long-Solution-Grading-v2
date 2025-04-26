from second import get_shows

def get_table_sorted():
    shows = get_shows()
    return sorted(shows.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    table_sorted = get_table_sorted()
    print(table_sorted)
