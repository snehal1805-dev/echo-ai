from app.services.embedding_service import search_similar


def retrieve_context(query: str, top_k: int = 5):
    """
    Retrieve the most relevant document chunks
    for a user's question.
    """

    results = search_similar(query, top_k)

    documents = results.get("documents", [])

    if not documents:
        return []

    return documents[0]