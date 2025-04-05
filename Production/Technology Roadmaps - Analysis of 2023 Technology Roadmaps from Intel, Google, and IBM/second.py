from io import BytesIO
from PyPDF2 import PdfReader
from first import get_resp

def get_pdf():
    resp = get_resp()
    return PdfReader(BytesIO(resp.content))

if __name__ == "__main__":
    pdf = get_pdf()
    print(len(pdf.pages))
