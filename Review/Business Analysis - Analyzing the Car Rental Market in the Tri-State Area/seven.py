from _six import get_soup_ny

def get_headers():
    # identify header tags with "Airport Locations"
    soup_ny = get_soup_ny()
    return soup_ny.find_all(["h3"])

if __name__ == "__main__":
    headers = get_headers()
    print([(h.text, h.name) for h in headers[:15]])
