from app.services.retrieval_service import retrieve_context
from app.services.llm_service import ask_llm


def chat_with_documents(question: str):
    # 1. Search ChromaDB
    chunks = retrieve_context(question)

    # 2. Ask Gemini
    answer = ask_llm(question, chunks)

    return answer