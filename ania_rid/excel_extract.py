from PyPDF2 import PdfReader

def extract_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    result = text.strip()
    print("PDF DONE")
    return result


