from sqlalchemy import Column, DateTime, Float, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Cattle(Base, BaseColumnsMixin):
    __tablename__ = "cattle"
    identifier = Column(String(10), unique=True, nullable=False)
    herd_id = Column(UUID(as_uuid=True), ForeignKey("herds.id"), nullable=True)

    herd = relationship("Herd", back_populates="cattle")
    weight_history = relationship("WeightHistory", back_populates="cattle", cascade="all, delete-orphan")

class WeightHistory(Base, BaseColumnsMixin):
    __tablename__ = "weight_history"
    cattle_id = Column(UUID(as_uuid=True), ForeignKey("cattle.id"), nullable=False)
    weight = Column(Float, nullable=False)
    measured_at = Column(DateTime(timezone=True), nullable=False) 

    cattle = relationship("Cattle", back_populates="weight_history")
