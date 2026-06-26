from app.rag.loader import load_medical_documents
from app.rag.chunker import split_documents
from app.rag.vectorstore import create_vector_store


def rebuild_knowledge_base():
    """
    Reload PDFs and rebuild ChromaDB.
    """

    documents = load_medical_documents()

    chunks = split_documents(documents)

    create_vector_store(chunks)

    return {
        "documents": len(documents),
        "chunks": len(chunks)
    }