from pydantic import BaseModel, Field, model_validator
from typing import Optional


class ServerCreateRequest(BaseModel):
    name: str = Field(..., description="VM name")

    flavor_id: str = Field(..., description="Flavor ID")
    network_id: str = Field(..., description="Network ID")

    image_id: Optional[str] = Field(
        default=None,
        description="Image ID"
    )

    volume_id: Optional[str] = Field(
        default=None,
        description="Boot volume ID"
    )

    @model_validator(mode="after")
    def validate_boot_source(self):

        has_image = self.image_id is not None
        has_volume = self.volume_id is not None

        if has_image == has_volume:
            raise ValueError(
                "Exactly one of image_id or volume_id must be specified"
            )

        return self

class ServerResponse(BaseModel):
    id: str
    name: str
    status: str
    
class ServerActionResponse(BaseModel):
    id: str
    status: str