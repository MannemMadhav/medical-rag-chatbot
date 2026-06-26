import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.loader import load_medical_documents
from app.rag.chunker import split_documents
from app.rag.vectorstore import create_vector_store


def main():
    documents = load_medical_documents()

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    print(f"Total documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")

    print("\nVector store created successfully!")

    print(vector_store)


if __name__ == "__main__":
    main()