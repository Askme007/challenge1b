from scorer import score_chunks

def select_relevant_sections(pdf_chunks, persona, job, top_k=5):
    query = f"{persona}. {job}"
    extracted_sections = []
    subsection_analysis = []

    importance_counter = 1

    for pdf in pdf_chunks:
        filename = pdf["filename"]
        chunks = pdf["chunks"]

        scored = score_chunks(chunks, query)
        for entry in scored[:top_k]:
            extracted_sections.append({
                "document": filename,
                "section_title": entry.get("heading", entry["text"][:60]),
                "importance_rank": importance_counter,
                "page_number": entry["page"]
            })

            subsection_analysis.append({
                "document": filename,
                "refined_text": entry["text"],
                "page_number": entry["page"]
            })

            importance_counter += 1

    return {
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
