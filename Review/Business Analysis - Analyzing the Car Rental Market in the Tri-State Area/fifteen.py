import requests

def get_r():
    url_location = "https://www.kayak.com/mvm/ajax/carLocation?loc=New+York"
    return requests.get(url_location)

if __name__ == "__main__":
    print(get_r().status_code)
