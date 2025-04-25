from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageStat
import io, requests
img1 = Image.open(io.BytesIO(requests.get("https://os.ys613.cn/doc/preview/20241016/88fa08c5340c32d214ed8313e39a2cae.png").content))
print(img1.size, img1.mode)
