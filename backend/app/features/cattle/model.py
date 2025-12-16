from sqlalchemy import Column, String

from app.db.base import Base
from app.db.mixins import BaseColumnsMixin


class Cattle(Base, BaseColumnsMixin):
    __tablename__ = "cattle"
    identifier = Column(String(10), unique=True, nullable=False)
