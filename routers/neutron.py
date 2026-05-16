from fastapi import APIRouter, Request
from openstack_client import get_conn

router = APIRouter()


@router.get("/networks")
def list_networks(request: Request):
    conn = get_conn(request)

    return {
        "networks": [
            {
                "id": n.id,
                "name": n.name,
                "status": n.status
            }
            for n in conn.network.networks()
        ]
    }