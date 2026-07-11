from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Text

from app.database.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    original_filename = Column(String(255), nullable=False)

    stored_filename = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    file_type = Column(String(50), nullable=False)

    file_size = Column(Integer, nullable=False)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship("User", back_populates="resources")
    extracted_text = Column(Text, nullable=True)