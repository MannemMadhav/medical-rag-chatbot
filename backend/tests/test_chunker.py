import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.loader import load_medical_documents
from app.rag.chunker import split_documents


def main():
    documents = load_medical_documents()

    chunks = split_documents(documents)

    print(f"Total documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")

    if chunks:
        print("\nFirst chunk preview:\n")
        print(chunks[0].page_content)


if __name__ == "__main__":
    main()