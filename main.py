from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import openstack

@asynccontextmanager
async def lifespan(app: FastAPI):

    conn = openstack.connect(cloud='mycloud')
    app.state.openstack_conn = conn
    print("OpenStack connection established")
    yield
    # Shutdown: Close Connection
    app.state.openstack_conn.close()
    print("OpenStack connection closed")

app = FastAPI(lifespan=lifespan)

@app.get("/servers")
def list_servers(request: Request):
    # Access the connection
    conn = app.state.openstack_conn
    servers = [server.name for server in conn.compute.servers()]
    return {"servers": servers}
