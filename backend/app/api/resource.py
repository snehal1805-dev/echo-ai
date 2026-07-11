from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.models.user_model import User
from app.schemas.resource_schema import ResourceResponse
from app.services.resource_service import save_file

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.post(
    "/upload",
    response_model=ResourceResponse
)
def upload_resource(
    title: str = Form(...),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resource = save_file(
        db=db,
        file=file,
        title=title,
        user_id=current_user.id
    )

    return resource