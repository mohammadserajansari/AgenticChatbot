from pathlib import Path
from llama_cpp import Llama
import asyncio

BASE_DIR = Path(__file__).resolve().parents[2]  # agentic-chatbot/app/core
MODEL_PATH = BASE_DIR / "models" / "Phi-3-mini-4k-instruct-q4.gguf"

llm = None

def load_llm():
    global llm
    if llm is None:
        llm = Llama(
            model_path=str(MODEL_PATH),
            n_threads=4
        )
    return llm

async def generate_stream(prompt, max_tokens=1024, temperature=0.3, top_p=0.9):
    """
    Async generator to stream tokens from llama-cpp-python
    """
    model = load_llm()
    # llama-cpp-python streaming
    for token_dict in model.create_completion(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stream=True
    ):
        # each token_dict has 'choices' -> [{'text': ...}]
        token_text = token_dict["choices"][0]["text"]
        if token_text:
            yield token_text
        await asyncio.sleep(0)  # async-friendly
