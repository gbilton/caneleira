from typing import List, Optional
from uuid import UUID
from datetime import datetime

from fastapi import HTTPException
from app.features.cattle.model import Cattle, WeightHistory
from app.features.cattle.repository import CattleRepository, WeightHistoryRepository
from app.features.cattle.schema import CattleCreate, CattleRead, CattleUpdate


class CattleService:
    def __init__(self, repository: CattleRepository):
        self.repository: CattleRepository = repository

    def create(self, data: CattleCreate) -> Cattle:
        exists = self.repository.get_by_identifier(data.identifier)
        if exists:
            raise HTTPException(status_code=400, detail=f"Cattle with identifier {data.identifier} already exists")
        return self.repository.create(data)

    def get_all(self, herd_id: Optional[UUID] = None) -> List[CattleRead]:
        all_cattle = self.repository.get_all(herd_id=herd_id)
        return [CattleRead.model_validate(cattle) for cattle in all_cattle]
    
    def get_by_id(self, cattle_id: UUID) -> CattleRead:
        cattle = self.repository.get_by_id(cattle_id)
        if not cattle:
            raise HTTPException(status_code=404, detail=f"Cattle id {cattle_id} not found")
        return CattleRead.model_validate(cattle)
    
    def update(self, cattle_id: UUID, updates: CattleUpdate) -> CattleRead:
        cattle = self.repository.get_by_id(cattle_id)
        if not cattle:
            raise HTTPException(status_code=404, detail=f"Cattle id {cattle_id} not found")
        updated_cattle = self.repository.update(cattle, updates)
        return CattleRead.model_validate(updated_cattle)
    
    def delete(self, cattle_id: UUID) -> None:
        cattle = self.repository.get_by_id(cattle_id)  
        if not cattle:
            raise HTTPException(status_code=404, detail=f"Cattle id {cattle_id} not found")
        self.repository.delete(cattle)

class WeightHistoryService:
    def __init__(self, repository: WeightHistoryRepository):
        self.repository: WeightHistoryRepository = repository

    def create(self, cattle_id: UUID, weight: float, measured_at: datetime) -> WeightHistory:
        return self.repository.create(cattle_id, weight, measured_at)

    def get_all(self, cattle_id: UUID):
        return self.repository.get_all(cattle_id)
    
    def delete(self, cattle_id: UUID, weight_history_record_id: UUID) -> None:
        weight_history_record = self.repository.get_by_id(cattle_id, weight_history_record_id)
        if not weight_history_record:
            raise HTTPException(status_code=404, detail=f"Weight history record id {weight_history_record_id} for cattle id {cattle_id} not found")
        self.repository.delete(weight_history_record)

