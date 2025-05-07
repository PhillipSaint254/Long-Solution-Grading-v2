from PIL import Image
import requests, io, base64, numpy as np
from third import get_url

def get_img():
    url = get_url()
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))

if __name__ == "__main__":
    img = get_img()
    print(img.size)
    