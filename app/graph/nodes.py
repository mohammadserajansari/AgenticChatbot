# from app.rag.ingest import ingest_file
# from app.rag.vectorstore import load_vectorstore
# from app.core.model import load_llm
# import asyncio

# llm = load_llm()

# class UploadNode:
#     """Async ingestion node"""
#     async def run(self, file_path: str):
#         return await ingest_file(file_path)

# class QueryNode:
#     """Async query node"""
#     async def run(self, query: str):
#         vectorstore = load_vectorstore()
#         if vectorstore is None:
#             # fallback to LLM
#             raw = llm(query, max_tokens=512, temperature=0.3, top_p=0.9)
#             return {"mode": "llm", "response": raw["choices"][0]["text"].strip()}

#         # RAG mode
#         docs = vectorstore.similarity_search(query, k=4)
#         context = "\n\n".join(d.page_content for d in docs)

#         prompt = f"""
# You are an AI assistant.
# Answer the question using ONLY the context below.
# If the context does not contain the answer, say:
# "I could not find this information in the uploaded document."

# Context:
# {context}

# Question:
# {query}

# Answer in a complete, well-structured paragraph:
# """
#         raw = llm(prompt, max_tokens=1024, temperature=0.3, top_p=0.9)
#         response = raw["choices"][0]["text"].strip()
#         return {"mode": "rag", "response": response}

############

from app.rag.ingest import ingest_file
from app.rag.vectorstore import load_vectorstore
from app.core.model import load_llm
import asyncio

llm = load_llm()
vectorstore = None  # global, will reload if new file ingested

class UploadNode:
    async def run(self, file_path: str):
        await ingest_file(file_path)
        global vectorstore
        vectorstore = load_vectorstore()
        return {"status": "uploaded", "file": file_path}

class QueryNode:
    async def run(self, question: str):
        global vectorstore
        if vectorstore is None:
            # normal LLM chat
            raw = llm(question, max_tokens=256, temperature=0.3)
            return raw["choices"][0]["text"].strip()

        # RAG chat
        docs = vectorstore.similarity_search(question, k=3)
        context = "\n\n".join(d.page_content for d in docs)

        # handle context window safely
        max_context_tokens = 512
        prompt_tokens = len((context + question).split())
        max_tokens = max_context_tokens - prompt_tokens
        if max_tokens <= 0:
            context = "\n".join(context.split("\n")[-200:])
            max_tokens = max_context_tokens - len(question.split())

        prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.
If the context does not contain the answer, say:
"I could not find this information in the uploaded document."

Context:
{context}

Question:
{question}

Answer in a complete paragraph:
"""
        raw = llm(prompt, max_tokens=max_tokens, temperature=0.3)
        return raw["choices"][0]["text"].strip()
