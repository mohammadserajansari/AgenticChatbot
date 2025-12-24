
####################
# from langchain_huggingface import HuggingFaceEmbeddings

# def get_embeddings():
#     return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



########
# from langchain_community.embeddings import SentenceTransformerEmbeddings
# from sentence_transformers import SentenceTransformer
# from pathlib import Path
# import torch

# BASE_DIR = Path(__file__).resolve().parents[2]

# # agentic-chatbot/models/
# MODEL_DIR = BASE_DIR / "models"

# # HuggingFace cache-style folder (THIS EXISTS)
# LOCAL_MODEL_PATH = (
#     MODEL_DIR / "models--sentence-transformers--all-MiniLM-L6-v2"
# )

# def download_model():
#     """
#     Downloads the model once and ensures a valid local path
#     """
#     if not LOCAL_MODEL_PATH.exists():
#         print("Downloading SentenceTransformer model locally...")
#         SentenceTransformer(
#             MODEL_NAME,
#             cache_folder=str(MODEL_DIR)
#         )
#     else:
#         print(f"Using local embedding model at {LOCAL_MODEL_PATH}")

#     return str(LOCAL_MODEL_PATH)


# def get_embeddings():
#     device = "mps" if torch.backends.mps.is_available() else "cpu"
#     local_path = download_model()

#     return SentenceTransformerEmbeddings(
#         model_name=local_path,
#         model_kwargs={"device": device},
#         encode_kwargs={"normalize_embeddings": True}
#     )


# from pathlib import Path
# import torch
# from langchain_community.embeddings import SentenceTransformerEmbeddings

# BASE_DIR = Path(__file__).resolve().parents[2]

# HF_CACHE_MODEL_DIR = (
#     BASE_DIR
#     / "models"
#     / "models--sentence-transformers--all-MiniLM-L6-v2"
#     / "snapshots"
# )

# def _find_snapshot_dir() -> Path:
#     if not HF_CACHE_MODEL_DIR.exists():
#         raise FileNotFoundError(
#             f"HuggingFace cache not found at {HF_CACHE_MODEL_DIR}"
#         )

#     snapshots = [p for p in HF_CACHE_MODEL_DIR.iterdir() if p.is_dir()]
#     if not snapshots:
#         raise FileNotFoundError("No snapshot found inside HF cache directory")

#     # use first snapshot (only one normally exists)
#     return snapshots[0]

# def get_embeddings():
#     snapshot_path = _find_snapshot_dir()

#     device = "mps" if torch.backends.mps.is_available() else "cpu"

#     return SentenceTransformerEmbeddings(
#         model_name=str(snapshot_path),
#         model_kwargs={"device": device},
#         encode_kwargs={"normalize_embeddings": True},
#     )


###################

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
