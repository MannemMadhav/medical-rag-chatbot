from langchain_community.embeddings import HuggingFaceEmbeddings

from app.core.config import settings


def get_embedding_model():
    """
    Load embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )

    return embeddings