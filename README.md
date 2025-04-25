# AIVerseAgents

AIVerseAgents is a modular, multi-agent AI framework designed to serve both customer-facing and internal business needs.  
It leverages large language models (LLMs), Retrieval-Augmented Generation (RAG), and vector databases to provide intelligent, context-aware responses.  
The project includes a FastAPI-powered web interface for seamless interaction with different AI agents.

---

## 🚀 Features

- **Multi-Agent Architecture**: Supports multiple AI agents (e.g., AI1 for customer service, AI2 for internal assistance) with isolated vector stores and document ingestion pipelines.
- **RAG Integration**: Utilizes RAG techniques to enhance response accuracy by retrieving relevant documents from vector databases.
- **FastAPI Web Interface**: Provides a user-friendly web interface to interact with different AI agents.
- **Modular Design**: Easily extendable to add more agents or integrate additional functionalities.
- **Secure Configuration**: Uses `.env` files to manage API keys and sensitive configurations securely.

---

## 📂 Project Structure

AIVerseAgents/ 
├── agents/     
│   │── ai1_assistant.py  
│   └── ai2_assistant.py 
├── api/        
│   │── server.py 
├── core/       
│   ├── file_ingestion.py
│   |── embedding_pipelines.py
│   ├── llm_router.py
│   └── vector_store.py 
├── docs/       
│   ├── ai1/.. 
│   └── ai2/..         
├── ragloaders/ 
│   ├── ingest_ai1_docs.py 
│   └── ingest_ai2_docs.py  
├── static/ 
│ └── styles.css 
├── templates/ 
│ └── chat.html 
├── .env 
├── chat_ai1.py 
├── chat_ai2.py 
├── requirements.txt 
└── README.md

---

## 🛠️ Installation

### 1. Clone the Repository

git clone https://github.com/dkaltsios/AIVerseAgents.git
cd AIVerseAgents

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file in the root directory and add your API keys:
COHERE_API_KEY=your-cohere-api-key
TOGETHER_API_KEY=your-together-api-key

---

## 📄 Document Ingestion
Before running the agents, ingest the relevant documents into their respective vector stores.

### Prepare Documents
Place your .txt or .pdf documents in the appropriate directories:

Customer-facing documents: docs/ai1/

Internal documents: docs/ai2/

### Run Ingestion Scripts
python ragloaders/ingest_ai1_docs.py
python ragloaders/ingest_ai2_docs.py

---

## 💬 Running the Web Interface
### Start the FastAPI Server
uvicorn api.server:app --reload

### Access the Web Interface
Open your browser and navigate to:
http://localhost:8000

### Interact with Agents
Use the dropdown menu to select either the Customer Service Agent (AI1) or the Internal Assistant (AI2), enter your query, and click "Ask" to receive a response.

---

## 🧪 Testing Agents via CLI
Alternatively, you can interact with the agents using the command-line interface:

### AI1 (Customer Service Agent)
python chat_ai1.py
### AI2 (Internal Assistant)
python chat_ai2.py

---

## 🧱 Adding New Agents
To add a new AI agent:
Create a new assistant script in the agents/ directory (e.g., ai3_assistant.py).
Implement the necessary logic for the new agent.
Add a corresponding document ingestion script in ragloaders/ (e.g., ingest_ai3_docs.py).
Update the FastAPI server (api/server.py) to include routes for the new agent.
Modify the HTML template (templates/chat.html) to add the new agent to the dropdown menu.

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