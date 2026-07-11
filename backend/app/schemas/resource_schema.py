from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ResourceResponse(BaseModel):

    id: int

    title: str

    original_filename: str

    file_type: str

    file_size: int

    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)
    