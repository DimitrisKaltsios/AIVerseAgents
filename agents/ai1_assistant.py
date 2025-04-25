# This is for AI1 Assistant Customer Chatbot Agent

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from core.llm_router import get_llm

def create_customer_agent():
    llm = get_llm()
    memory = ConversationBufferMemory()

    # Custom prompt for a customer service chatbot
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""
You are AI1, a helpful and polite customer service chatbot for our company. 
Your job is to answer customer questions clearly, professionally, and empathetically.

Previous conversation:
{history}

Customer: {input}
AI1:"""
    )

    return ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt
    )

def chat_with_customer(query: str, agent=None):
    if not agent:
        agent = create_customer_agent()
    return agent.run(query), agent