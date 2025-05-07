import pytesseract, numpy as np, io, requests, PIL.Image as Image
from eight import get_img1

def get_boxes_str():
    img1 = get_img1()
    # Convert to grayscale
    gray_img = img1.convert('L')

    # Save to check; we can't show but we can run boxes
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    return pytesseract.image_to_boxes(gray_img, config=custom_config)

if __name__ == "__main__":
    boxes_str = get_boxes_str()
    print(boxes_str[:200])
