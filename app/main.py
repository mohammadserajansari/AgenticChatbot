from fastapi import FastAPI
from app.api import upload, chat

app = FastAPI(title="Agentic Chatbot")

app.include_router(upload.router)
app.include_router(chat.router)
