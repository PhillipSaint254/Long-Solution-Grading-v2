import requests

def get_r():
    url_test = "https://www.kayak.com/s/apisearch"
    return requests.get(url_test)

if __name__ == "__main__":
    print(get_r().status_code)
    