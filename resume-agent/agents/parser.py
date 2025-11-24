import pdfplumber
from pathlib import Path

def extract_text(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    pdf_path = "data/candidate_raw.pdf"
    out_path = "data/extracted.txt"

    extracted = extract_text(pdf_path)
    Path(out_path).write_text(extracted, encoding="utf-8")
    print("Extracted text saved to data/extracted.txt")
