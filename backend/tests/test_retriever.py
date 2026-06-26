import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.retriever import get_retriever


def main():
    retriever = get_retriever()

    query = "What is diabetes?"

    documents = retriever.invoke(query)

    print(f"Query: {query}")
    print(f"Retrieved documents: {len(documents)}")

    for index, document in enumerate(documents, start=1):
        print(f"\n--- Result {index} ---\n")
        print(document.page_content[:500])


if __name__ == "__main__":
    main()