from PIL import Image
import requests, io, base64, numpy as np

def get_img():
    url = "https://s2.guitarworld.com.cn/upload/pu_qupupic/326175/view/af49012f7c90c0c28180d7138efb9b87.png"
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))

if __name__ == "__main__":
    img = get_img()
    print(img.size)
