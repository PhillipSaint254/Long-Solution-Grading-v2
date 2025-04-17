import requests

def get_collections():
    return ["degods", "okay_bears", "famous_fox_federation", "solana_monkey_business", "degenerate_ape_academy"]


def get_api_template():
    return "https://api-mainnet.magiceden.dev/v2/collections/{}/stats"


def get_floor_prices():
    floor_prices = {}
    collections = get_collections()
    api_template = get_api_template()
    for c in collections:
        url = api_template.format(c)
        resp = requests.get(url).json()
        floor_prices[c] = resp.get("floorPrice")  # lamports
    return floor_prices

if __name__ == "__main__":
    print(get_floor_prices())
