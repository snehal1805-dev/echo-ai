from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user
from app.schemas.user_schema import UserLogin, Token
from app.services.user_service import login_user
from app.core.dependencies import get_current_user
from app.models.user_model import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = create_user(db, user)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return new_user

@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        user.email,
        user.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return token

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user