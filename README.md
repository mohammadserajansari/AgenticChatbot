🤖 AgenticChatbot

AgenticChatbot is a production-ready, local AI ecosystem designed for high-performance Retrieval-Augmented Generation (RAG). Built with FastAPI and LangChain, it enables users to interact with local LLMs (like LLaMA) while maintaining complete data privacy and context awareness.

✨ Features

Local LLM Support: Run models locally (e.g., LLaMA via llama-cpp-python) without external API costs.

RAG Integration: Context-aware responses using FAISS vector storage and HuggingFace embeddings (all-MiniLM-L6-v2).

Streaming Output: Real-time token streaming for long answers and better UX.

Fully Asynchronous: High-concurrency API powered by FastAPI and asyncio.

Automated Ingestion: Seamless file ingestion and semantic document chunking.

Production Structure: Modular folder architecture for scalability and clean development.

📂 Project Structure

AgenticChatbot/
├── app/
│   ├── api/            # Endpoint logic (chat, upload, auth, eval)
│   ├── core/           # LLM integration & Embedding generation
│   ├── graph/          # RAG + query pipelines (LangGraph/Nodes)
│   ├── rag/            # Document ingestion & Vectorstore management
│   ├── utils/          # Shared helper functions
│   ├── main.py         # FastAPI application entrypoint
│   └── schemas.py      # Request and response validation models
├── data/               # Raw source files for ingestion (git-ignored)
├── models/             # GGUF model files (git-ignored)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
└── README.md           # Documentation


🛠️ Setup Instructions

1. Clone the Repository

git clone [https://github.com/mohammadserajansari/AgenticChatbot.git](https://github.com/mohammadserajansari/AgenticChatbot.git)
cd AgenticChatbot


2. Environment Setup

We recommend using Conda for environment management:

# Create environment
conda create -n aiagent python=3.12 -y
conda activate aiagent

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt


3. Model & Data Preparation

Models: Download your LLM in .gguf format and place it in the models/ folder.

Data: Place your PDF, TXT, or markdown files to be indexed in the data/ folder.

4. Run the Application

Start the FastAPI server using Uvicorn:

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


🔌 API Reference

Access the interactive API documentation (Swagger UI) at: http://127.0.0.1:8000/docs

Chat (RAG-enabled)

POST /chat/

{
  "message": "Tell me about the project's architecture."
}


Retrieves relevant chunks from FAISS and generates a streaming response.

Document Upload

POST /upload/
Upload files via multipart/form-data to trigger automatic chunking and indexing.

🐳 Docker Support

Build and run the application in a isolated container:

# Build the image
docker build -t agentic-chatbot .

# Run the container
docker run -d -p 8000:8000 --name agentic-chatbot agentic-chatbot


🤝 Contributing

Contributions are welcome! Please follow these steps:

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License

Distributed under the MIT License. See LICENSE for more information.

Developed with ❤️ by Mohammad Seraj