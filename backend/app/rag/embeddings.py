import os
from langchain_jina import JinaEmbeddings


def get_embedding_model():
    return JinaEmbeddings(
        jina_api_key=os.getenv("JINA_API_KEY"),
        model_name="jina-embeddings-v3",
    )