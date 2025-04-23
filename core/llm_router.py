import os
from langchain_openai import ChatOpenAI  


def get_llm():
    return ChatOpenAI(
        model_name="mistralai/Mistral-7B-Instruct-v0.1",
        openai_api_base="https://api.together.xyz/v1", # ADD API KEY WHEN DONE
        openai_api_key=os.getenv("TOGETHER_API_KEY"), # ADD API KEY WHEN DONE
        temperature=0
    )
