from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Herd(Base, BaseColumnsMixin):
    __tablename__ = "herds"

    name = Column(String(50), unique=True, nullable=False)

    cattle = relationship("Cattle", back_populates="herd")
