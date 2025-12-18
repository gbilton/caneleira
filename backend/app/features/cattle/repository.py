from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Optional, Sequence
from .model import Cattle, WeightHistory
from .schema import CattleCreate, CattleUpdate
from uuid import UUID
from datetime import datetime, timezone


class CattleRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create a new cattle
    def create(self, cattle_in: CattleCreate) -> Cattle:
        cattle = Cattle(**cattle_in.model_dump())
        self.db.add(cattle)
        self.db.commit()
        self.db.refresh(cattle)
        return cattle

    # Get all cattle (exclude soft-deleted)
    def get_all(self, herd_id: Optional[UUID] = None) -> Sequence[Cattle]:
        stmt = select(Cattle).where(Cattle.deleted_at.is_(None))
        if herd_id:
            stmt = stmt.where(Cattle.herd_id == herd_id)
        return self.db.execute(stmt).scalars().all()

    # Get by ID
    def get_by_id(self, cattle_id: UUID) -> Optional[Cattle]:
        stmt = select(Cattle).where(Cattle.id == cattle_id, Cattle.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().first()

    # Get by identifier
    def get_by_identifier(self, identifier: str) -> Optional[Cattle]:
        stmt = select(Cattle).where(Cattle.identifier == identifier, Cattle.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().first()

    # Update existing cattle
    def update(self, cattle: Cattle, updates: CattleUpdate) -> Cattle:
        for key, value in updates.model_dump(exclude_unset=True).items():
            setattr(cattle, key, value)
        cattle.updated_at = datetime.now(tz=timezone.utc)
        self.db.commit()
        self.db.refresh(cattle)
        return cattle

    # Soft delete
    def delete(self, cattle: Cattle) -> None:
        cattle.deleted_at = datetime.now(tz=timezone.utc)
        self.db.commit()

class WeightHistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, cattle_id: UUID, weight: float, measured_at: datetime) -> WeightHistory:
        weight_history_record = WeightHistory(
            cattle_id=cattle_id,
            weight=weight,
            measured_at=measured_at
        )
        self.db.add(weight_history_record)
        self.db.commit()
        return weight_history_record

    def get_all(self, cattle_id: UUID) -> Sequence[WeightHistory]:
        stmt = select(WeightHistory).where(WeightHistory.cattle_id == cattle_id, WeightHistory.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().all()
    
    def get_by_id(self, cattle_id: UUID, id: UUID) -> Optional[WeightHistory]:
        stmt = select(WeightHistory).where(WeightHistory.id == id, WeightHistory.cattle_id == cattle_id, WeightHistory.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().first()
    
    def delete(self, weight_history_record: WeightHistory) -> None:
        weight_history_record.deleted_at = datetime.now(tz=timezone.utc)
        self.db.commit()