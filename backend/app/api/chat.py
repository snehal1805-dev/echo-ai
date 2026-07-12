from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import chat_with_documents

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = chat_with_documents(request.question)

    return ChatResponse(
        answer=answer
    )

@router.post("/chat")
def chat(request: ChatRequest):
    answer = chat_with_documents(request.question)

    return {
        "answer": answer
    }