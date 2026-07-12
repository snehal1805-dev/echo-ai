from fastapi import FastAPI

from app.database.database import Base, engine
from app.api.auth import router as auth_router
from app.models.resource_model import Resource
from app.api.resource import router as resource_router
from app.api.chat import router as chat_router

# Import models so SQLAlchemy knows about them
from app.models.user_model import User

app = FastAPI(
    title="Echo AI API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(resource_router)
app.include_router(chat_router)
# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Echo AI Backend Running 🚀"
    }