from fastapi import APIRouter, Request
from openstack_client import get_conn

router = APIRouter()


@router.get("/images")
def list_images(request: Request):
    conn = get_conn(request)

    return {
        "images": [
            {
                "id": i.id,
                "name": i.name,
                "status": i.status
            }
            for i in conn.image.images()
        ]
    }