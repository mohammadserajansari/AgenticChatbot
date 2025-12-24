# from asyncio import create_task
# from typing import List
# from app.graph.nodes import UploadNode, QueryNode
# from app.utils.file import save_upload_file

# class LangGraphPipeline:
#     """Full automated pipeline: upload -> ingest -> query"""

#     async def upload_files(self, files: List):
#         paths = []
#         for file in files:
#             file_path = save_upload_file(file)
#             paths.append(file_path)
#             create_task(UploadNode().run(file_path))  # async background ingestion
#         return {"status": "uploaded", "files": paths}

#     async def query(self, query: str):
#         result = await QueryNode().run(query)
#         return result

################
from app.graph.nodes import UploadNode, QueryNode

class LangGraphPipeline:
    def __init__(self):
        self.upload_node = UploadNode()
        self.query_node = QueryNode()

    async def upload_file(self, file_path: str):
        return await self.upload_node.run(file_path)

    async def query(self, question: str):
        return await self.query_node.run(question)
