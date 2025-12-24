# # from fastapi import APIRouter, UploadFile, File
# # from typing import List
# # from app.graph.pipeline import LangGraphPipeline

# # router = APIRouter(prefix="/upload", tags=["Upload"])
# # pipeline = LangGraphPipeline()

# # @router.post("/")
# # async def upload_files(files: List[UploadFile] = File(...)):
# #     result = await pipeline.upload_files(files)
# #     return result


# ################

# from fastapi import APIRouter, UploadFile, BackgroundTasks
# from app.graph.pipeline import LangGraphPipeline
# from app.utils.file import save_file

# router = APIRouter(prefix="/upload", tags=["Upload"])
# pipeline = LangGraphPipeline()

# @router.post("/")
# async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
#     content = await file.read()
#     file_path = save_file(content, file.filename)
#     background_tasks.add_task(pipeline.upload_file, file_path)
#     return {"status": "processing", "file": file.filename}


############

from fastapi import APIRouter, UploadFile, BackgroundTasks
from pathlib import Path
import shutil
from app.rag.ingest import ingest_file

router = APIRouter()
UPLOAD_DIR = Path(__file__).resolve().parents[2] / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/")
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    background_tasks.add_task(ingest_file, str(file_path))
    return {"status": "processing", "filename": file.filename}
