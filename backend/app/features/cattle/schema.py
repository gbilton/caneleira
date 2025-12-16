from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class CattleCreate(BaseModel):
    identifier: str

    model_config = {
        "from_attributes": True
    }

class CattleRead(BaseModel):
    id: UUID
    identifier: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }

class CattleUpdate(BaseModel):
    identifier: str

class CattleDelete(BaseModel):
    id: str 

class CattleResponse(BaseModel):
    id: UUID
    identifier: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
