import os
from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv

load_dotenv()


def get_llm():
    return ChatOpenAI(
        model_name="mistralai/Mistral-7B-Instruct-v0.1",
        openai_api_base="https://api.together.xyz/v1", 
        openai_api_key=os.getenv("TOGETHER_API_KEY"), 
        temperature=0
    )
