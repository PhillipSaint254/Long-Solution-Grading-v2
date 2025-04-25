import pytesseract
from _six import get_img

def get_text():
    img = get_img()
    return pytesseract.image_to_string(img)

if __name__ == "__main__":
    text = get_text()
    print(text[:500])
