import requests, io, base64, numpy as np, PIL.Image as Image
response = requests.get("https://os.ys613.cn/doc/preview/20241016/88fa08c5340c32d214ed8313e39a2cae.png")
print("status", response.status_code, "first bytes", response.content[:20])
