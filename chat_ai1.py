from langchain.chains import RetrievalQA
from core.llm_router import get_llm
from core.vector_store import get_vectorstore

def create_customer_agent():
    retriever = get_vectorstore("db/ai1_customer").as_retriever()
    llm = get_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def chat_with_customer(query: str, agent=None):
    if not agent:
        agent = create_customer_agent()
    return agent.invoke({"query": query})["result"], agent
def run_cli():
    print("🤖 AI1 Customer Chatbot is ready! Type 'exit' to quit.")
    agent = None
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response, agent = chat_with_customer(query, agent)
        print("AI1:", response)

if __name__ == "__main__":
    run_cli()

# To load just one .txt file in vector store, use code below
# from core.file_ingestion import extract_text_from_pdf
# from core.vector_store import ingest_docs

# if __name__ == "__main__":
#     # Only run once to ingest the file
#     text = extract_text_from_pdf("docs/ai1/shipping_faq.txt")
#     ingest_docs([text], index_path="db/ai1_customer")
#     print("📄 shipping_faq.txt ingested into AI1.")

# If I want to load multiple files in vector store, use code below
# import os
# from core.file_ingestion import extract_text_from_pdf
# from core.vector_store import ingest_docs

# for filename in os.listdir("docs/ai1"):
#     if filename.endswith(".pdf"):
#         path = os.path.join("docs/ai1", filename)
#         text = extract_text_from_pdf(path)
#         ingest_docs([text], index_path="db/ai1_customer")

