from fastapi import Request, FastAPI, HTTPException
from contextlib import asynccontextmanager
import openstack

@asynccontextmanager
async def lifespan(app: FastAPI):

    conn = openstack.connect(cloud='mycloud')
    app.state.openstack_conn = conn

    print("OpenStack connection established")

    yield

    app.state.openstack_conn = None
    print("OpenStack connection released")

def get_conn(request: Request):
    conn = request.app.state.openstack_conn

    if conn is None:
        raise HTTPException(
            status_code=500,
            detail="OpenStack connection unavailable"
        )

    return conn