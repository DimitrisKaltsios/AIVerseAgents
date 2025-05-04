# import requests
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from core.llm_router import get_llm
from core.file_ingestion import extract_text_from_pdf

def create_explainer_agent():
    llm = get_llm()
    memory = ConversationBufferMemory()

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""
You are AI3, a document explainer assistant. Your job is to:
1. Summarize the content.
2. Explain it in clear, simple terms.

Previous conversation:
{history}

Document Content:
{input}

AI3 Response:
"""
    )

    return ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt
    )

def explain(text: str, agent=None) -> dict:
    if not agent:
        agent = create_explainer_agent()

    explanation = agent.run(text)

    # For now, we will not translate the explanation to Greek.
    # if translate:
    #     translated = translate_to_greek(explanation)
    # else:
    #     translated = "❌ Skipped"

    return {
        "summary_explanation": explanation,
        # "translated": translated
    }

def load_and_explain(path: str, translate_to_greek: bool = False) -> dict:
    if path.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file format. Use .pdf or .txt")

    return explain(text)

# If we want to translate to greek, we need to create docker container for libretranslate to run locally, bellow is demonstration for api requests (paid)
# def translate_to_greek(text: str) -> str:
#     url = "https://libretranslate.com/translate"
#     payload = {
#         "q": text,
#         "source": "en",
#         "target": "el",
#         "format": "text"
#     }
#     headers = {
#         "User-Agent": "Mozilla/5.0",
#         "Accept": "application/json",
#         "Content-Type": "application/x-www-form-urlencoded"
#     }

#     response = requests.post(url, data=payload, headers=headers)

#     if response.status_code == 200:
#         return response.json().get("translatedText", "[Translation failed]")
#     else:
#         return f"[Translation error: status code {response.status_code} - {response.text}]"
