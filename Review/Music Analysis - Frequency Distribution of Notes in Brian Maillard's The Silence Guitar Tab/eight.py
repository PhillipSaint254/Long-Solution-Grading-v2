from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageStat
import io, requests

def get_img1():
    return Image.open(io.BytesIO(requests.get("https://os.ys613.cn/doc/preview/20241016/88fa08c5340c32d214ed8313e39a2cae.png").content))

if __name__ == "__main__":
    img1 = get_img1()
    print(img1.size, img1.mode)
