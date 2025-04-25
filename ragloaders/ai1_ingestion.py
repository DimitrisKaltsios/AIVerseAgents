import os
from dotenv import load_dotenv
from core.file_ingestion import extract_text_from_pdf
from core.vector_store import ingest_docs

load_dotenv()
DOCS_PATH = "docs/ai1"
INDEX_PATH = "db/ai1_customer"

def ingest_customer_documents():
    print("📥 Starting ingestion of customer-facing documents...")
    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".pdf") or filename.endswith(".txt"):
            path = os.path.join(DOCS_PATH, filename)
            print(f" - Ingesting {filename}...")
            text = extract_text_from_pdf(path)
            ingest_docs([text], index_path=INDEX_PATH)
    print("✅ All AI1 customer documents ingested.")

if __name__ == "__main__":
    ingest_customer_documents()
