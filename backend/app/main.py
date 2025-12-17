from fastapi import FastAPI
from app.features.cattle.router import router as cattle_router
from app.features.herd.router import router as herd_router

app = FastAPI(title="My API")

app.include_router(cattle_router, prefix="/cattle")
app.include_router(herd_router, prefix="/herd")
