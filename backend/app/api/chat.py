from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.logger import logger
from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter()

rag_service = None


def get_rag_service():
    global rag_service

    if rag_service is None:
        rag_service = RAGService()

    return rag_service


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    logger.info("Chat request received")
    logger.info(f"Question: {request.question}")

    service = get_rag_service()

    result = service.ask(request.question)

    logger.info("Response generated successfully")

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
    )


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    logger.info("Streaming chat request received")
    logger.info(f"Question: {request.question}")

    service = get_rag_service()

    def generate():
        for chunk in service.stream(request.question):
            yield chunk

        logger.info("Streaming response completed")

    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )