import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from app.rag.retriever import get_retriever
from app.rag.prompt import MEDICAL_RAG_PROMPT
from app.rag.generator import get_llm


def main():
    question = "What is diabetes?"

    retriever = get_retriever()

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = MEDICAL_RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    print("\nQUESTION:\n")
    print(question)

    print("\nANSWER:\n")
    print(response.content)


if __name__ == "__main__":
    main()