from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional
from .model import Cattle
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
    def get_all(self, herd_id: Optional[UUID] = None) -> List[Cattle]:
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
