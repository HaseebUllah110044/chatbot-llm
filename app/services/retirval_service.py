from sqlalchemy.orm import Session
from app.services.embeddingservice import EmbeddingService
from app.repositories.retrivalrepo import search_similar_chunks


embedding_service = EmbeddingService()


def retrieve_chunks(
    query:str,
    db:Session,
    limit:int=5
):

    query_embedding = embedding_service.create_embedding(
        query
    )

    chunks = search_similar_chunks(
        query_embedding,
        db,
        limit
    )

    return chunks