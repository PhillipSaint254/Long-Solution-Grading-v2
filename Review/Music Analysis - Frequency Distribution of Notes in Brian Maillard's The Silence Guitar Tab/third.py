import requests, io, numpy as np

def get_url():
    return "https://s2.guitarworld.com.cn/upload/pu_qupupic/326175/view/af49012f7c90c0c28180d7138efb9b87.png"

if __name__ == "__main__":
    url = get_url()
    data = requests.get(url).content[:100]
    print(len(data), data[:10])
