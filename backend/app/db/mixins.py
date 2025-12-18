import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as SA_UUID
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class BaseColumnsMixin:
    id: Mapped[uuid.UUID] = mapped_column(SA_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
