from fastapi import FastAPI
from openstack_client import lifespan
from routers import nova, neutron, glance

app = FastAPI(lifespan=lifespan)

app.include_router(nova.router, tags=['Nova'], prefix="/api/nova")
app.include_router(neutron.router, tags=['Neutron'], prefix="/api/neutron")
app.include_router(glance.router, tags=['Glance'], prefix="/api/glance")