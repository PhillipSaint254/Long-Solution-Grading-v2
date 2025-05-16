import requests

def get_html_ny():
    url_ny = "https://www.enterprise.com/en/car-rental/locations/us/ny.html"
    return requests.get(url_ny).text

if __name__ == "__main__":
    html_ny = get_html_ny()
    print(len(html_ny))
