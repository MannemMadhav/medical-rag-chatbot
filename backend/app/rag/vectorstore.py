from langchain_community.vectorstores import Chroma

from app.core.config import settings
from app.rag.embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create and persist ChromaDB vector store.
    """

    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(settings.VECTOR_DB_PATH)
    )

    return vector_store