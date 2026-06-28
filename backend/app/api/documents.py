from pathlib import Path
import shutil
from app.core.config import settings
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.document_service import rebuild_knowledge_base

router = APIRouter()

UPLOAD_DIR = Path(settings.PDF_DATA_PATH)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    rebuild_stats = rebuild_knowledge_base()

    return {
        "message": "File uploaded and indexed successfully",
        "filename": file.filename,
        "documents": rebuild_stats["documents"],
        "chunks": rebuild_stats["chunks"],
    }


@router.get("/documents")
async def list_documents():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    documents = []

    for pdf in sorted(UPLOAD_DIR.glob("*.pdf")):
        documents.append(
            {
                "name": pdf.name,
                "size_bytes": pdf.stat().st_size,
            }
        )

    return {
        "count": len(documents),
        "documents": documents,
    }


@router.delete("/documents/{filename}")
async def delete_document(filename: str):
    print("=" * 60)
    print("DELETE REQUEST")
    print("filename:", repr(filename))
    print("UPLOAD_DIR:", UPLOAD_DIR)
    print("Exists:", UPLOAD_DIR.exists())

    files = list(UPLOAD_DIR.glob("*"))
    print("FILES:")
    for f in files:
        print(" ->", repr(f.name))

    file_path = UPLOAD_DIR / filename
    print("Target:", file_path)
    print("Target exists:", file_path.exists())
    print("=" * 60)

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Document not found: {filename}",
        )

    file_path.unlink()

    rebuild_stats = rebuild_knowledge_base()

    return {
        "message": "Document deleted successfully",
        "documents": rebuild_stats["documents"],
        "chunks": rebuild_stats["chunks"],
    }