from langchain_groq import ChatGroq

from app.core.config import settings


def get_llm():
    """
    Create and return the Groq LLM.
    """

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0,
        streaming=True,
    )

    return llm