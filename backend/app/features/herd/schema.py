from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class HerdCreate(BaseModel):
    name: str

    model_config = {"from_attributes": True}


class HerdRead(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None

    model_config = {"from_attributes": True}


class HerdUpdate(BaseModel):
    name: str


class HerdDelete(BaseModel):
    id: str


class HerdResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
