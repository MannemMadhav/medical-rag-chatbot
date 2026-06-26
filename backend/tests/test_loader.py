import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.loader import load_medical_documents


def main():
    documents = load_medical_documents()

    print(f"Total documents loaded: {len(documents)}")

    if documents:
        print("\nFirst document preview:\n")
        print(documents[0].page_content[:500])


if __name__ == "__main__":
    main()