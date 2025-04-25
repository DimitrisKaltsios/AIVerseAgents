from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from agents.ai1_assistant import chat_with_customer
from agents.ai2_assistant import ask_question as ask_internal

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, query: str = Form(...), agent_type: str = Form(...)):
    if agent_type == "ai1":
        response, _ = chat_with_customer(query)
    elif agent_type == "ai2":
        response = ask_internal(query)
    else:
        response = "Invalid agent selected."
        agent_type = "unknown"

    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "response": response,
            "query": query,
            "agent_type": agent_type
        }
    )