from PIL import Image
import pytesseract, cv2, numpy as np, requests, io, pandas as pd

# Download image
url1 = "http://os.ys613.cn/doc/preview/20241016/88fa08c5340c32d214ed8313e39a2cae.png"
img_data = requests.get(url1).content
img = Image.open(io.BytesIO(img_data))

# Convert to grayscale
gray = img.convert('L')

# Use pytesseract to get boxes (digits only)
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
boxes_str = pytesseract.image_to_boxes(gray, config=custom_config)

print(boxes_str[:1000])
