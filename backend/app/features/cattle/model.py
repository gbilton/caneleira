from sqlalchemy import Column, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Cattle(Base, BaseColumnsMixin):
    __tablename__ = "cattle"
    identifier = Column(String(10), unique=True, nullable=False)
    herd_id = Column(UUID(as_uuid=True), ForeignKey("herds.id"), nullable=True)

    herd = relationship("Herd", back_populates="cattle")
