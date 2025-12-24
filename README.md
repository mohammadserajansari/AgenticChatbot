# 🤖 AgenticChatbot

AgenticChatbot is a production-ready, local AI ecosystem designed for high-performance Retrieval-Augmented Generation (RAG). Built with FastAPI and LangChain, it enables users to interact with local LLMs (like LLaMA) while maintaining complete data privacy and context awareness.

---

## ✨ Features

- 🏠 **Fully Local Execution:** Run models locally (e.g., LLaMA via `llama-cpp-python`) without external API costs or data leaks.  
- 📚 **Advanced RAG Pipeline:** Context-aware responses using FAISS vector storage and HuggingFace embeddings (`all-MiniLM-L6-v2`).  
- ⚡ **Streaming Output:** Real-time token streaming for long answers and a smooth user experience.  
- 🚀 **Asynchronous API:** High-concurrency support powered by FastAPI and Python's asyncio.  
- 📂 **Automated Ingestion:** Seamless file ingestion, semantic document chunking, and vector indexing.  
- 🏗️ **Production Structure:** Modular folder architecture designed for scalability and clean code maintenance.  

---

## 📂 Project Structure

```text
AgenticChatbot/
├── app/
│   ├── api/            # Route handlers (chat, upload)
│   ├── core/           # LLM logic and embedding configurations
│   ├── graph/          # RAG + query pipelines (LangGraph/Nodes)
│   ├── rag/            # Vectorstore management and document ingestion
│   ├── utils/          # Shared helper functions
│   ├── main.py         # FastAPI entry point
│   └── schemas.py      # Pydantic models for request/response validation
├── data/               # Raw document storage (PDFs, TXT, etc. - git-ignored)
├── models/             # Local GGUF model files (git-ignored)
├── requirements.txt    # Project dependencies
├── Dockerfile          # Container orchestration
└── README.md           # Documentation
```


## 🛠️ Setup & Run

1. Clone the repository
```
git clone https://github.com/mohammadserajansari/AgenticChatbot.git
cd AgenticChatbot

```
2. Create and activate Conda environment
```bash
conda create -n aiagent python=3.12 -y
conda activate aiagent
```
3. Download Phi-3 Mini GGUF model

```bash
huggingface-cli download \
  microsoft/Phi-3-mini-4k-instruct-gguf \
  phi-3-mini-4k-instruct-q4.gguf \
  --local-dir models \
  --local-dir-use-symlinks False
```
This will save the model here:
```text
models/phi-3-mini-4k-instruct-q4.gguf
```
4. Next, download the embedding model to use it offline.
```text
sentence-transformers/all-MiniLM-L6-v2
```
5. Upgrade pip and install dependencies
```python
pip install --upgrade pip
pip install -r requirements.txt
```

6. Add your documents for RAG in 'data/' folder
PDF, TXT, or Markdown files will be indexed automatically

7. Run FastAPI server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
8. Access API docs in your browser
```bash
http://127.0.0.1:8000/docs
```
🔌 API Reference
Chat (RAG-enabled)
POST /chat/
JSON Example:
```json
{
  "message": "What are the core components of this system?"
}
```
Returns real-time streaming response from the local LLM using retrieved context.

Document Upload
POST /upload/
Accepts multipart/form-data. Triggers automatic chunking and FAISS index update.

9. 🐳 Docker Deployment
\n Build Docker image
```bash
docker build -t agentic-chatbot .
```

Run container
```bash
docker run -d -p 8000:8000 --name agentic-chatbot agentic-chatbot
```

## 🤝 Contributing

1. Fork the Project  
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the Branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

---

Developed with ❤️ by [Mohammad Seraj](https://www.linkedin.com/in/ansariserajmd/)


