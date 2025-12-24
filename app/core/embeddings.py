from pathlib import Path
import torch
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parents[2]

HF_MODEL_ROOT = (
    BASE_DIR
    / "models"
    / "models--sentence-transformers--all-MiniLM-L6-v2"
    / "snapshots"
)

def _get_snapshot_path() -> str:
    snapshots = [p for p in HF_MODEL_ROOT.iterdir() if p.is_dir()]
    if not snapshots:
        raise RuntimeError("No SentenceTransformer snapshot found")
    return str(snapshots[0])

def get_embeddings():
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    model_path = _get_snapshot_path()

    return HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True},
    )
