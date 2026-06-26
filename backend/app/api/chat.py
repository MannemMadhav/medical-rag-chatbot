from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.logger import logger
from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter()

rag_service = RAGService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    logger.info("Chat request received")
    logger.info(f"Question: {request.question}")

    result = rag_service.ask(request.question)

    logger.info("Response generated successfully")

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    logger.info("Streaming chat request received")
    logger.info(f"Question: {request.question}")

    def generate():

        for chunk in rag_service.stream(request.question):
            yield chunk

        logger.info("Streaming response completed")

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )