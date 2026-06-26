from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.core.exception_handler import global_exception_handler

app = FastAPI(
    title="Medical RAG Chatbot",
    version="1.0.0",
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Medical RAG Chatbot API Running",
    }


app.include_router(chat_router)
app.include_router(health_router)
app.include_router(documents_router)