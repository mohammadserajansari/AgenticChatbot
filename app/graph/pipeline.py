from app.graph.nodes import UploadNode, QueryNode

class LangGraphPipeline:
    def __init__(self):
        self.upload_node = UploadNode()
        self.query_node = QueryNode()

    async def upload_file(self, file_path: str):
        return await self.upload_node.run(file_path)

    async def query(self, question: str):
        return await self.query_node.run(question)
