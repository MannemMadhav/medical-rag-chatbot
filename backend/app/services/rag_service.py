from app.rag.retriever import get_retriever
from app.rag.prompt import MEDICAL_RAG_PROMPT
from app.rag.generator import get_llm
from app.services.memory_service import get_memory


class RAGService:

    def __init__(self):
        self.retriever = get_retriever()
        self.llm = get_llm()
        self.memory = get_memory()

    def ask(self, question: str):

        documents = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = MEDICAL_RAG_PROMPT.format(
            context=context,
            question=question
        )

        response = self.llm.invoke(prompt)

        self.memory.save_context(
            {"input": question},
            {"output": response.content}
        )

        sources = []

        for doc in documents:

            source = doc.metadata.get("source", "Unknown")

            filename = source.split("\\")[-1]
            filename = filename.split("/")[-1]

            if filename not in sources:
                sources.append(filename)

        return {
            "answer": response.content,
            "sources": sources
        }

    def stream(self, question: str):

        documents = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = MEDICAL_RAG_PROMPT.format(
            context=context,
            question=question
        )

        full_answer = ""

        for chunk in self.llm.stream(prompt):

            if chunk.content:

                full_answer += chunk.content

                yield chunk.content

        self.memory.save_context(
            {"input": question},
            {"output": full_answer}
        )   