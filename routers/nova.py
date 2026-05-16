from fastapi import APIRouter, HTTPException, status, Request
from openstack_client import get_conn
from schemas.server import ServerCreateRequest, ServerResponse, ServerActionResponse

router = APIRouter()

@router.get("/server_list")
def list_servers(request: Request):

    conn = get_conn(request)

    servers = [
        {
            "id": server.id,
            "name": server.name,
            "status": server.status
        }
        for server in conn.compute.servers()
    ]

    return {"servers": servers}


@router.get("/flavors_list")
def list_flavors(request: Request):

    conn = get_conn(request)

    flavors = [
        {
            "id": flavor.id,
            "name": flavor.name,
            "ram": flavor.ram,
            "vcpus": flavor.vcpus,
            "disk": flavor.disk
        }
        for flavor in conn.compute.flavors()
    ]

    return {"flavors": flavors}

@router.post("/create_server", response_model=ServerResponse)
def create_server(request: Request, payload: ServerCreateRequest):

    conn = get_conn(request)

    server = conn.compute.create_server(
        name=payload.name,
        image_id=payload.image_id,
        flavor_id=payload.flavor_id,
        networks=[
            {"uuid": payload.network_id}
        ]
    )

    return ServerResponse(
        id=server.id,
        name=server.name,
        status=server.status,
        image_id=payload.image_id,
        flavor_id=payload.flavor_id,
        addresses=getattr(server, "addresses", None)
    )


@router.delete("/delete_server/{server_id}", response_model=ServerActionResponse)
def delete_server(request: Request, server_id: str):

    conn = get_conn(request)

    server = conn.compute.find_server(server_id)

    if not server:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    conn.compute.delete_server(server, ignore_missing=False)

    return ServerActionResponse(
        id=server_id,
        status="DELETE_IN_PROGRESS"
    )