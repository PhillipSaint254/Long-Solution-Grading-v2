from four import get_img
import pytesseract

def get_text():
    img = get_img()
    return pytesseract.image_to_string(img)

if __name__ == "__main__":
    text = get_text()
    print(text[:500])