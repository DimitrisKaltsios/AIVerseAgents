from langchain_community.vectorstores import Chroma
from core.embedding_pipeline import get_embedding_model
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_vectorstore(index_path="db/ai2_internal"):
    embedding = get_embedding_model()
    return Chroma(persist_directory=index_path, embedding_function=embedding)

def ingest_docs(texts: list[str], index_path="db/ai2_internal"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents(texts)
    vs = Chroma.from_documents(documents=docs, embedding=get_embedding_model(), persist_directory=index_path)
    vs.persist()
