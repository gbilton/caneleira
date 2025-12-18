from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, String, UUID as SA_UUID
from uuid import UUID 
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Cattle(Base, BaseColumnsMixin):
    __tablename__ = "cattle"
    identifier: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    herd_id: Mapped[UUID | None] = mapped_column(SA_UUID(as_uuid=True), ForeignKey("herds.id"), nullable=True)

    herd = relationship("Herd", back_populates="cattle")
    weight_history = relationship("WeightHistory", back_populates="cattle", cascade="all, delete-orphan")

class WeightHistory(Base, BaseColumnsMixin):
    __tablename__ = "weight_history"
    cattle_id: Mapped[UUID] = mapped_column(SA_UUID(as_uuid=True), ForeignKey("cattle.id"), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    measured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    cattle = relationship("Cattle", back_populates="weight_history")
