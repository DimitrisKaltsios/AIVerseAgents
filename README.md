# AIVerseAgents

AIVerseAgents is a modular, multi-agent AI framework designed to serve both customer-facing and internal business needs.  
It leverages large language models (LLMs), Retrieval-Augmented Generation (RAG), and vector databases to provide intelligent, context-aware responses.  
The project includes a FastAPI-powered web interface for seamless interaction with different AI agents.

---

## 🚀 Features

- **Multi-Agent Architecture**: Supports multiple AI agents:
  - **AI1**: Customer Service Agent
  - **AI2**: Internal Business Assistant
  - **AI3**: Document Explainer (summarizes .txt and .pdf files)
- **RAG Integration**: Utilizes RAG techniques to enhance response accuracy by retrieving relevant documents from vector databases.
- **FastAPI Web Interface**: Provides a user-friendly web interface to interact with different AI agents.
- **Modular Design**: Easily extendable to add more agents or integrate additional functionalities.
- **Secure Configuration**: Uses `.env` files to manage API keys and sensitive configurations securely.

---

## 📂 Project Structure

```
AIVerseAgents/ 
├── agents/     
│   ├── ai1_assistant.py  
│   ├── ai2_assistant.py 
│   └── ai3_explainer.py
├── api/        
│   └── server.py 
├── core/       
│   ├── file_ingestion.py
│   ├── embedding_pipelines.py
│   ├── llm_router.py
│   └── vector_store.py 
├── docs/       
│   ├── ai1/.. 
│   ├── ai2/..
│   └── ai3/..       
├── ragloaders/ 
│   ├── ingest_ai1_docs.py 
│   ├── ingest_ai2_docs.py
│   └── ingest_ai3_docs.py  
├── static/ 
│   └── styles.css 
├── templates/ 
│   └── chat.html 
├── .env 
├── chat_ai1.py 
├── chat_ai2.py 
├── chat_ai3.py
├── requirements.txt 
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/dkaltsios/AIVerseAgents.git
cd AIVerseAgents
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
COHERE_API_KEY=your-cohere-api-key
TOGETHER_API_KEY=your-together-api-key
```

---

## 📄 Document Ingestion
Before running the agents, ingest the relevant documents into their respective vector stores.

### Prepare Documents
Place your `.txt` or `.pdf` documents in the appropriate directories:
- Customer-facing documents: `docs/ai1/`
- Internal documents: `docs/ai2/`
- Legal or explainable documents: `docs/ai3/`

### Run Ingestion Scripts
```bash
python ragloaders/ingest_ai1_docs.py
python ragloaders/ingest_ai2_docs.py
python ragloaders/ingest_ai3_docs.py
```

---

## 💬 Running the Web Interface

### Start the FastAPI Server
```bash
uvicorn api.server:app --reload
```

### Access the Web Interface
Open your browser and navigate to:
```
http://localhost:8000
```

### Interact with Agents
Use the dropdown menu to select:
- Customer Service Agent (AI1)
- Internal Assistant (AI2)
- Document Explainer (AI3)

For AI3, upload a `.txt` or `.pdf` file and click "Ask" to receive a detailed explanation.

---

## 🧪 Testing Agents via CLI

You can also interact with the agents using the command-line interface:

```bash
# AI1 (Customer Service Agent)
python chat_ai1.py

# AI2 (Internal Assistant)
python chat_ai2.py

# AI3 (Document Explainer)
python chat_ai3.py
```

---

## 🧱 Adding New Agents

To add a new AI agent:
1. Create a new assistant script in the `agents/` directory (e.g., `ai4_social.py`).
2. Implement the logic for the new agent.
3. Add a document ingestion script in `ragloaders/` (e.g., `ingest_ai4_docs.py`) if needed.
4. Update `api/server.py` to handle the new route.
5. Add the agent to `templates/chat.html` for web UI access.

---

## 📌 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📞 Contact
For any inquiries or support, please open an issue on the GitHub repository.

---
