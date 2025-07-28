import fitz
import os
from heading_extractor import extract_outline

def extract_text_chunks(pdf_dir):
    pdf_data = []

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_dir, filename)
            doc = fitz.open(path)

            outline_data = extract_outline(path)  # Use Round 1A
            headings = outline_data["outline"]

            # Group by headings
            chunks = []
            for i in range(len(headings)):
                start_page = headings[i]["page"]
                end_page = (
                    headings[i + 1]["page"] if i + 1 < len(headings) else doc.page_count
                )
                text = ""
                for p in range(start_page, end_page):
                    page = doc[p]
                    text += page.get_text()

                chunks.append({
                    "text": text.strip(),
                    "page": start_page,
                    "heading": headings[i]["text"]
                })

            pdf_data.append({
                "filename": filename,
                "chunks": chunks
            })

    return pdf_data
