import requests
import pandas as pd, numpy as np, io, textwrap

def get_text():
    url = "https://raw.githubusercontent.com/Mabdou11/Activity-Recognition-skeleton-datasets/master/kard_realworld/a18_s01_e01_realworld.txt"
    return requests.get(url).text

if __name__ == "__main__":
    text = get_text()
    print(text[:200])
