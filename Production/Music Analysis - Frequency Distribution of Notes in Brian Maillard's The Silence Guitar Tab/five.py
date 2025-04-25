import requests, io, numpy as np
url = "https://s2.guitarworld.com.cn/upload/pu_qupupic/326175/view/af49012f7c90c0c28180d7138efb9b87.png"
data = requests.get(url).content[:100]
print(len(data), data[:10])
