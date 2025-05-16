import requests

def get_r():
    url = "https://www.kayak.com/New-York-Car-Rentals.15830.cars"
    return requests.get(url)

if __name__ == "__main__":
    r = get_r()
    print(len(r.text[:1000]), r.status_code)
