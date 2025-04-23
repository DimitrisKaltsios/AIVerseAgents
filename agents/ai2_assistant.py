from langchain.chains import RetrievalQA
from core.vector_store import get_vectorstore
from core.llm_router import get_llm

def create_internal_agent():
    retriever = get_vectorstore().as_retriever()
    llm = get_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_question(query: str):
    agent = create_internal_agent()
    return agent.invoke({"query": query})["result"]
