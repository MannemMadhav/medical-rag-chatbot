from langchain_community.vectorstores import Chroma

from app.core.config import settings
from app.rag.embeddings import get_embedding_model


def get_retriever():
    """
    Load the Chroma vector database and create
    a production-ready retriever.
    """

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=str(settings.VECTOR_DB_PATH),
        embedding_function=embeddings,
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 8,
            "lambda_mult": 0.5,
        },
    )

    return retriever