from seven import get_soup_ny

def count_locations(soup):
    counts = {}
    for header in soup.find_all("h3"):
        title = header.get_text(strip=True)
        if "Locations" in title:  # includes Airport, Exotics, Neighborhood
            location_count = 0
            # iterate over next siblings until the next h3
            for sib in header.find_next_siblings():
                if sib.name == "h3":
                    break
                # count <a> within <li> or <p>
                links = sib.find_all("a")
                # Each list item seems to have <a>
                location_count += len(links)
            counts[title] = location_count
    return counts

if __name__ == "__main__":
    soup_ny = get_soup_ny()
    print(count_locations(soup_ny))
