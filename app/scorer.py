from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_chunks(chunks, query):
    # Embed the query once
    query_embedding = model.encode([query])[0]

    scored = []
    for chunk in chunks:
        text = chunk["text"]
        chunk_embedding = model.encode([text])[0]
        score = cosine_similarity([query_embedding], [chunk_embedding])[0][0]
        scored.append({
            "text": text,
            "page": chunk["page"],
            "score": float(score)
        })

    return sorted(scored, key=lambda x: -x["score"])
