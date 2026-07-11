import os
import shutil
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resource_model import Resource

from app.services.text_extraction_service import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.chunking_service import chunk_text
from app.services.embedding_service import store_embeddings

UPLOAD_DIR = "uploads"


def save_file(
    db: Session,
    file: UploadFile,
    title: str,
    user_id: int
):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    extension = file.filename.split(".")[-1]

    stored_filename = f"{uuid.uuid4()}.{extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        stored_filename
    )

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Clean text
    cleaned_text = clean_text(extracted_text)

    # Chunk text
    chunks = chunk_text(cleaned_text)

    # Save resource in MySQL
    resource = Resource(
        title=title,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path=file_path,
        file_type=file.content_type,
        file_size=os.path.getsize(file_path),
        user_id=user_id,
        extracted_text=cleaned_text
    )

    db.add(resource)
    db.commit()
    db.refresh(resource)

    # Store embeddings in ChromaDB
    store_embeddings(resource.id, chunks)

    return resource