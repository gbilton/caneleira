from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional
from .model import Herd
from .schema import HerdCreate, HerdUpdate
from uuid import UUID
from datetime import datetime, timezone


class HerdRepository:
    def __init__(self, db: Session):
        self.db = db

    # Create a new herd
    def create(self, herd_in: HerdCreate) -> Herd:
        herd = Herd(**herd_in.model_dump())
        self.db.add(herd)
        self.db.commit()
        self.db.refresh(herd)
        return herd

    # Get all herds (exclude soft-deleted)
    def get_all(self) -> List[Herd]:
        stmt = select(Herd).where(Herd.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().all()

    # Get by ID
    def get_by_id(self, herd_id: UUID) -> Optional[Herd]:
        stmt = select(Herd).where(Herd.id == herd_id, Herd.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().first()

    # Get by name
    def get_by_name(self, name: str) -> Optional[Herd]:
        stmt = select(Herd).where(Herd.name == name, Herd.deleted_at.is_(None))
        return self.db.execute(stmt).scalars().first()

    # Update existing herd
    def update(self, herd: Herd, updates: HerdUpdate) -> Herd:
        for key, value in updates.model_dump(exclude_unset=True).items():
            setattr(herd, key, value)
        herd.updated_at = datetime.now(tz=timezone.utc)
        self.db.commit()
        self.db.refresh(herd)
        return herd

    # Soft delete
    def delete(self, herd: Herd) -> None:
        herd.deleted_at = datetime.now(tz=timezone.utc)
        self.db.commit()
