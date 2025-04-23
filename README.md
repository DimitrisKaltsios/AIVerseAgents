
# 🧠 AI2 Internal Assistant

AI2 is a powerful internal business assistant that allows employees to query company knowledge securely and intelligently. It leverages:

- 🔍 **Document search with vector embeddings** (Cohere)
- 💬 **LLM responses with RAG** (Together.ai)
- 🌐 **User-friendly web interface** (FastAPI + HTML)
- 🔐 Runs locally, keeps your data private

---

## 📁 Project Structure

```
ai-business-suite/
├── agents/                  # AI agent logic
├── core/                    # LLM router, embeddings, vector store
├── api/                     # FastAPI server
├── templates/               # HTML frontend
├── static/                  # CSS styles
├── db/                      # ChromaDB persistence
├── main.py                  # CLI interface (optional)
├── .env                     # API keys here
├── requirements.txt
├── README.md                # You're here!
```

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai2-assistant.git
cd ai2-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you're using **Python 3.10+**

---

### 3. Add API Keys

Create a `.env` file in the root:

```
COHERE_API_KEY=your-cohere-key
TOGETHER_API_KEY=your-together-key
```

Get keys:
- [Cohere](https://dashboard.cohere.com/)
- [Together](https://www.together.ai/)

---

### 4. Ingest Your First PDF

Place a document in the root directory and name it `sample.pdf`. The assistant will automatically ingest it when you launch it.

---

### 5. Run the Web Interface

```bash
uvicorn api.server:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🖥 Features

- 📄 PDF ingestion using PyMuPDF
- 🧠 Cohere embeddings + ChromaDB
- 💬 Together.ai for answering questions using Mistral or LLaMA 3
- 🖼 FastAPI + Jinja2 HTML frontend
- 🔄 Full RAG chain via LangChain

---

## 🔧 Customization

### Change the Model

Edit `core/llm_router.py`:

```python
model_name="mistralai/Mistral-7B-Instruct-v0.1"
```

You can try:
- `meta-llama/Llama-3-8b-chat-hf`
- `openchat/openchat-3.5-1210`
- See full list: https://api.together.ai/models

---

### Add More Documents

You can modify `main.py` or create a drag-and-drop UI for batch ingestion.

---

## 🧪 Test Locally

```bash
python main.py
```

Use the terminal to ask questions from your ingested data.

---

## ✨ Coming Soon Ideas

- Slack or MS Teams bot integration
- Upload-anywhere document support
- Admin dashboard for usage/stats
- Access control by department/user

---

## 🙌 Credits

Built using:
- [LangChain](https://www.langchain.com/)
- [Cohere](https://cohere.com/)
- [Together AI](https://www.together.ai/)
- [FastAPI](https://fastapi.tiangolo.com/)
