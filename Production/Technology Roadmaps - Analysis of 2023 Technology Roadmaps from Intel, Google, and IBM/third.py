from second import get_pdf

def get_text():
     pdf = get_pdf()
     return pdf.pages[0].extract_text()

if __name__ == "__main__":
    text = get_text()
    print(text)
