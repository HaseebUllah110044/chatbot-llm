from sqlalchemy.orm import Session
from app.services.retirval_service import retrieve_chunks



def build_knowledge_context(
    query:str,
    db:Session
):

    chunks = retrieve_chunks(
        query,
        db
    )
    print("TOTAL RETRIEVED CHUNKS:", len(chunks))

    for index, chunk in enumerate(chunks):
        print("====================")
        print("CHUNK NUMBER:", index)
        print("CHUNK ID:", chunk.ChunkID)
        print("DOCUMENT ID:", chunk.DocumentID)
        print("CONTENT LENGTH:", len(chunk.Content))
        print(chunk.Content[:500])

    context = "Relevant knowledge:\n\n"


    for chunk in chunks:

        context += chunk.Content
        context += "\n\n"


    return context