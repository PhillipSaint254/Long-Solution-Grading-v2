from five import get_html_ny
from bs4 import BeautifulSoup


def get_soup_ny():
    html_ny = get_html_ny()
    return BeautifulSoup(html_ny, "html.parser")

# Find all bullet items under Neighborhood Locations, Airport Locations, Exotics Locations
# We'll search for all <a> elements within those sections.
