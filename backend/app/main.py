from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.features.cattle.router import router as cattle_router
from app.features.herd.router import router as herd_router


app = FastAPI(title="My API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cattle_router)
app.include_router(herd_router)
