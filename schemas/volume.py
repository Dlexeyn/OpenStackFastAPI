from typing import Optional
from pydantic import BaseModel

class VolumeResponse(BaseModel):
    id: str
    name: Optional[str] = None
    status: str
    size: int