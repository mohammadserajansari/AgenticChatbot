# app/api/chat.py
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.rag.vectorstore import load_vectorstore
# from app.core.model import get_model
from app.core.model import load_llm as get_model
import asyncio

router = APIRouter()


# Request model
class ChatRequest(BaseModel):
    message: str


# RAG query helper
async def rag_query(user_input: str):
    try:
        db = load_vectorstore()
        docs = db.similarity_search(user_input, k=3)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"Context:\n{context}\n\nQuestion: {user_input}\nAnswer:"
    except Exception:
        prompt = f"Question: {user_input}\nAnswer:"
    return prompt


# Generator wrapper for streaming
async def generate_stream_async(prompt: str, max_tokens: int = 1024):
    """
    Wrap llama-cpp-python streaming into an async generator
    """
    model = get_model()  # returns a Llama instance
    # llama-cpp-python: use create_completion(stream=True)
    for token_dict in model.create_completion(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.95,
        stream=True
    ):
        # token_dict example: {'id': ..., 'object': 'text_completion', 'choices':[{'text': '...', ...}]}
        token_text = token_dict['choices'][0]['text']
        if token_text:
            yield token_text
        await asyncio.sleep(0)  # async-friendly


# Chat endpoint
@router.post("/chat/")
async def chat(request: ChatRequest):
    user_input = request.message
    prompt = await rag_query(user_input)

    async def streamer():
        async for token in generate_stream_async(prompt, max_tokens=1024):
            yield token

    return StreamingResponse(streamer(), media_type="text/plain")
