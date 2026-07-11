from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.jwt_handler import create_access_token

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):

    # Check if email already exists
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        return None

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db, email: str, password: str):

    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }