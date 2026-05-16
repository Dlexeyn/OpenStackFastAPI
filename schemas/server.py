from pydantic import BaseModel, Field
from typing import Optional, List


class ServerCreateRequest(BaseModel):
    name: str = Field(..., description="Name of the VM")

    image_id: str = Field(..., description="Glance image ID")
    flavor_id: str = Field(..., description="Nova flavor ID")
    network_id: str = Field(..., description="Neutron network ID")


class ServerResponse(BaseModel):
    id: str
    name: str
    status: str

    image_id: Optional[str] = None
    flavor_id: Optional[str] = None
    addresses: Optional[dict] = None

class ServerActionResponse(BaseModel):
    id: str
    status: str