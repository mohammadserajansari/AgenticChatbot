
# from app.core.embeddings import get_embeddings
# from langchain_community.vectorstores import FAISS

# def load_vectorstore():
#     index_file = os.path.join(INDEX_PATH, "index.faiss")
#     if not os.path.exists(index_file):
#         return None

#     return FAISS.load_local(
#         INDEX_PATH,
#         get_embeddings(),
#         allow_dangerous_deserialization=True
#     )


from langchain_community.vectorstores import FAISS
from pathlib import Path
from app.core.embeddings import get_embeddings

INDEX_PATH = Path(__file__).resolve().parents[2] / "data" / "index"

def load_vectorstore():
    return FAISS.load_local(INDEX_PATH, get_embeddings(), allow_dangerous_deserialization=True)
