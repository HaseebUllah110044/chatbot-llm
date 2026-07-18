from sqlalchemy.orm import Session

from app.models.documnet_chunks import DocumentChunk


def search_similar_chunks(
    embedding:list[float],
    db:Session,
    limit:int=5
):

    chunks = (
        db.query(DocumentChunk)
        .order_by(
            DocumentChunk.Embedding.cosine_distance(
                embedding
            )
        )
        .limit(limit)
        .all()
    )

    return chunks