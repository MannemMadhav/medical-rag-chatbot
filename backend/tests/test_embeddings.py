import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.loader import load_medical_documents
from app.rag.chunker import split_documents
from app.rag.embeddings import get_embedding_model


def main():
    documents = load_medical_documents()

    chunks = split_documents(documents)

    embeddings = get_embedding_model()

    vector = embeddings.embed_query(
        chunks[0].page_content
    )

    print(f"Total documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Embedding dimension: {len(vector)}")

    print("\nFirst 10 values:\n")
    print(vector[:10])


if __name__ == "__main__":
    main()