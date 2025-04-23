import os
from langchain_cohere.embeddings import CohereEmbeddings

def get_embedding_model():
    return CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        model="embed-multilingual-v3.0"
    )
