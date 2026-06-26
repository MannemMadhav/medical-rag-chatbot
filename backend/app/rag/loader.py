from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.core.config import settings


def load_medical_documents():
    """
    Load all PDF documents from the medical PDF directory.
    """

    pdf_directory = Path(settings.PDF_DATA_PATH)

    documents = []

    pdf_files = list(pdf_directory.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in {pdf_directory}"
        )

    for pdf_file in pdf_files:
        loader = PyPDFLoader(str(pdf_file))

        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    return documents