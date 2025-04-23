from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from core.embedding_pipeline import get_embedding_model

def get_vectorstore():
    embedding = get_embedding_model()
    return Chroma(persist_directory="db", embedding_function=embedding)

def ingest_docs(texts: list[str]):
    vs = get_vectorstore()
    docs = [Document(page_content=t) for t in texts]
    vs.add_documents(docs)
