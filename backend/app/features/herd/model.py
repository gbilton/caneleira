from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Herd(Base, BaseColumnsMixin):
    __tablename__ = "herds"

    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    cattle = relationship("Cattle", back_populates="herd")
