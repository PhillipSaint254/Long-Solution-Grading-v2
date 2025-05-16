from eight import count_locations
import requests
from bs4 import BeautifulSoup

def get_location_count(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    counts = count_locations(soup)
    total = sum(counts.values())
    return total, counts

if __name__ == "__main__":
    ny_total, ny_breakdown = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/ny.html")
    nj_total, nj_breakdown = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/nj.html")
    ct_total, ct_breakdown = get_location_count("https://www.enterprise.com/en/car-rental/locations/us/ct.html")
    print(ny_total, ny_breakdown, nj_total, nj_breakdown, ct_total, ct_breakdown)
