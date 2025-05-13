import requests

def get_text():
    response = requests.get("https://whattheforce.ca/feed/podcast/")
    return response.text

if __name__ == "__main__":
    text = get_text()
    print(len(text), text[:300])
