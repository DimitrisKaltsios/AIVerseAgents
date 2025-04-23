import os
from dotenv import load_dotenv
from agents.ai2_assistant import ask_question
from core.file_ingestion import extract_text_from_pdf
from core.vector_store import ingest_docs

load_dotenv()

def run_cli():
    print("\n🧠 AI2 Internal Assistant | Ask me anything about your company data!\n")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("AI2:", ask_question(q))

if __name__ == "__main__":
    # Optional: ingest a sample doc
    if os.path.exists("sample.pdf"):
        text = extract_text_from_pdf("sample.pdf")
        ingest_docs([text])
        print("📄 Sample PDF ingested.")
    run_cli()
