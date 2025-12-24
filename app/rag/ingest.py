from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embeddings
from pathlib import Path
import asyncio

INDEX_PATH = Path(__file__).resolve().parents[2] / "data" / "index"

async def ingest_file(file_path: str):
    if file_path.endswith(".pdf"):
        docs = PyPDFLoader(file_path).load()
    elif file_path.endswith(".txt"):
        docs = TextLoader(file_path).load()
    elif file_path.endswith(".csv"):
        docs = CSVLoader(file_path).load()
    elif file_path.endswith(".xlsx"):
        docs = UnstructuredExcelLoader(file_path).load()
    else:
        raise ValueError("Unsupported file type")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    emb = get_embeddings()
    db = FAISS.from_documents(chunks, emb)
    db.save_local(INDEX_PATH)
    return db
