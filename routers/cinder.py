from fastapi import APIRouter, HTTPException, Request

from openstack_client import get_conn
from schemas.volume import VolumeResponse

router = APIRouter()


@router.get("/volumes", response_model=list[VolumeResponse])
def list_volumes(request : Request):

    try:
        conn = get_conn(request)

        volumes = conn.block_storage.volumes()

        return [
            VolumeResponse(
                id=volume.id,
                name=volume.name,
                status=volume.status,
                size=volume.size
            )
            for volume in volumes
        ]

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch volumes: {str(ex)}"
        )