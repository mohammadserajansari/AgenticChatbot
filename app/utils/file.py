# import os
# from fastapi import UploadFile
# from uuid import uuid4

# UPLOAD_DIR = "data/uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# def save_upload_file(file: UploadFile):
#     ext = file.filename.split(".")[-1]
#     unique_name = f"{uuid4().hex}.{ext}"
#     file_path = os.path.join(UPLOAD_DIR, unique_name)
#     with open(file_path, "wb") as f:
#         f.write(file.file.read())
#     return file_path


##############

from pathlib import Path

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_file(file, filename: str):
    file_path = UPLOAD_DIR / filename
    with open(file_path, "wb") as buffer:
        buffer.write(file)
    return str(file_path)
