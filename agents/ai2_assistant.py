from langchain.chains import RetrievalQA
from core.vector_store import get_vectorstore
from core.llm_router import get_llm

def create_internal_agent():
    retriever = get_vectorstore("db/ai2_internal").as_retriever()
    llm = get_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_question(query: str):
    agent = create_internal_agent()
    return agent.invoke({"query": query})["result"]

# If I want to load multiple files in vector store, use code below
# import os
# for filename in os.listdir("docs/ai2"):
    # if filename.endswith(".pdf"):
    #     path = os.path.join("docs/ai2", filename)
    #     text = extract_text_from_pdf(path)
    #     ingest_docs([text], index_path="db/ai2_internal")