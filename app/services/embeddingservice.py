from openai import OpenAI
from app.core.config import setting


class EmbeddingService:

    def __init__(self):
        self.client = OpenAI(
            api_key=setting.OPENAI_API_KEY
        )

    def create_embedding(self, text: str) -> list[float]:

        response = self.client.embeddings.create(
            model=setting.EMBEDDING_MODEL,
            input=text,
            dimensions=setting.EMBEDDING_DIMENSION
        )

        return response.data[0].embedding