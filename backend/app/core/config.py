from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    JINA_API_KEY = os.getenv("JINA_API_KEY")

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "jina-embeddings-v3",
    )

    VECTOR_DB_PATH = Path(
        os.getenv(
            "VECTOR_DB_PATH",
            str(BASE_DIR / "data" / "vector_db")
        )
    )

    PDF_DATA_PATH = Path(
        os.getenv(
            "PDF_DATA_PATH",
            str(BASE_DIR / "data" / "raw" / "medical_pdfs")
        )
    )


settings = Settings()