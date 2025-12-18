from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CattleCreate(BaseModel):
    identifier: str
    herd_id: Optional[UUID] = None

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

class WeightHistoryCreate(BaseModel):
    cattle_id: UUID
    weight: float
    measured_at: datetime

    model_config = {
        "from_attributes": True
    }

class WeightHistoryRead(BaseModel):
    id: UUID
    cattle_id: UUID
    weight: float
    measured_at: datetime
    created_at: datetime

    model_config = {
        "from_attributes": True
    }   

class WeightHistoryResponse(BaseModel):
    id: UUID
    cattle_id: UUID
    weight: float
    measured_at: datetime
    created_at: datetime

    model_config = {
        "from_attributes": True
    }  

