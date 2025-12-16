from fastapi import FastAPI
from app.features.cattle.router import router as cattle_router

app = FastAPI(title="My API")

app.include_router(cattle_router, prefix="/cattle")
