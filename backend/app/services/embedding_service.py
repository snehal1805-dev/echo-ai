import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model (loads once when the app starts)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create / Open ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Create / Get collection
collection = client.get_or_create_collection(
    name="echo_resources"
)


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Generate vector embeddings for a list of text chunks.
    """

    embeddings = model.encode(chunks)

    return embeddings.tolist()


def store_embeddings(resource_id: int, chunks: list[str]):
    """
    Store chunks and their embeddings in ChromaDB.
    """

    if not chunks:
        return

    embeddings = generate_embeddings(chunks)

    ids = []
    metadatas = []

    for index, chunk in enumerate(chunks):
        ids.append(f"{resource_id}_{index}")

        metadatas.append(
            {
                "resource_id": str(resource_id),
                "chunk_index": index,
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search_similar(query: str, top_k: int = 5):
    """
    Search for the most relevant chunks in ChromaDB.
    """

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
    )

    return results