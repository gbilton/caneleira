from typing import List
from uuid import UUID

from fastapi import HTTPException
from app.features.herd.model import Herd
from app.features.herd.repository import HerdRepository
from app.features.herd.schema import HerdCreate, HerdRead, HerdUpdate


class HerdService:
    def __init__(self, repository: HerdRepository):
        self.repository: HerdRepository = repository

    def create(self, data: HerdCreate) -> Herd:
        exists = self.repository.get_by_name(data.name)
        if exists:
            raise HTTPException(
                status_code=400,
                detail=f"Herd with name {data.name} already exists",
            )
        return self.repository.create(data)

    def get_by_id(self, herd_id: UUID) -> HerdRead:
        herd = self.repository.get_by_id(herd_id)
        if not herd:
            raise HTTPException(
                status_code=404, detail=f"Herd id {herd_id} not found"
            )
        return HerdRead.model_validate(herd)

    def list_all(self) -> List[HerdRead]:
        all_herds = self.repository.get_all()
        return [HerdRead.model_validate(herd) for herd in all_herds]

    def update(self, herd_id: UUID, updates: HerdUpdate) -> HerdRead:
        herd = self.repository.get_by_id(herd_id)
        if not herd:
            raise HTTPException(
                status_code=404, detail=f"Herd id {herd_id} not found"
            )
        updated_herd = self.repository.update(herd, updates)
        return HerdRead.model_validate(updated_herd)

    def delete(self, herd_id: UUID) -> None:
        herd = self.repository.get_by_id(herd_id)
        if not herd:
            raise HTTPException(
                status_code=404, detail=f"Herd id {herd_id} not found"
            )
        self.repository.delete(herd)
