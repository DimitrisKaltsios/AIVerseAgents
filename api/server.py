from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from agents.ai1_assistant import chat_with_customer
from agents.ai2_assistant import ask_question as ask_internal
from agents.ai3_explainer import load_and_explain
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat(
    request: Request,
    agent_type: str = Form(...),
    query: str = Form(None),
    file: UploadFile = File(None)
):
    response = ""

    if agent_type == "ai1":
        response, _ = chat_with_customer(query or "")
    elif agent_type == "ai2":
        response = ask_internal(query or "")
    elif agent_type == "ai3" and file:
        try:
            contents = await file.read()
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)
            result = load_and_explain(temp_path)
            response = result["summary_explanation"]
            os.remove(temp_path)
        except Exception as e:
            response = f"Error: {e}"
    else:
        response = "Invalid agent selected or required input missing."
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
