import os
from dotenv import load_dotenv
from core.file_ingestion import extract_text_from_pdf
from core.vector_store import ingest_docs

load_dotenv()
DOCS_PATH = "docs/ai2"
INDEX_PATH = "db/ai2_internal"

def ingest_internal_documents():
    print("📥 Starting ingestion of internal company documents...")
    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".pdf") or filename.endswith(".txt"):
            path = os.path.join(DOCS_PATH, filename)
            print(f" - Ingesting {filename}...")
            text = extract_text_from_pdf(path)
            ingest_docs([text], index_path=INDEX_PATH)
    print("✅ All AI2 internal documents ingested.")

if __name__ == "__main__":
    ingest_internal_documents()