"""7import os
import json
from datetime import datetime
from extractor import extract_text_chunks
from selector import select_relevant_sections

INPUT_DIR = "input/documents"
PERSONA_FILE = "input/persona.txt"
JOB_FILE = "input/job.txt"
OUTPUT_DIR = "output"

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def main():
    persona = read_file(PERSONA_FILE)
    job = read_file(JOB_FILE)

    pdf_chunks = extract_text_chunks(INPUT_DIR)

    result = select_relevant_sections(pdf_chunks, persona, job)

    output = {
        "metadata": {
            "input_documents": [pdf["filename"] for pdf in pdf_chunks],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": result["extracted_sections"],
        "subsection_analysis": result["subsection_analysis"]
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "challenge1b_output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("✅ Output saved to output/challenge1b_output.json")

if __name__ == "__main__":
    main()
""" 

import os
import json
from datetime import datetime
from extractor import extract_text_chunks
from selector import select_relevant_sections

INPUT_DIR = "input/documents"
PERSONA_FILE = "input/persona.txt"
JOB_FILE = "input/job.txt"
OUTPUT_DIR = "output"

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def main():
    persona = read_file(PERSONA_FILE)
    job = read_file(JOB_FILE)

    pdf_chunks = extract_text_chunks(INPUT_DIR)

    result = select_relevant_sections(pdf_chunks, persona, job)

    output = {
        "metadata": {
            "input_documents": [pdf["filename"] for pdf in pdf_chunks],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": result["extracted_sections"],
        "subsection_analysis": result["subsection_analysis"]
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "challenge1b_output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("✅ Output saved to output/challenge1b_output.json")

if __name__ == "__main__":
    main()