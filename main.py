from fastapi import FastAPI, Request, HTTPException
from openstack_client import get_conn, lifespan
from routers import nova, neutron, glance

app = FastAPI(lifespan=lifespan)

app.include_router(nova.router, tags=['Nova'], prefix="/api/nova")
app.include_router(neutron.router, tags=['Neutron'], prefix="/api/neutron")
app.include_router(glance.router, tags=['Glance'], prefix="/api/glance")