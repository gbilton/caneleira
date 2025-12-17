from fastapi import Depends
from app.db.session import get_session
from .repository import HerdRepository
from .service import HerdService


def get_herd_service(
    session = Depends(get_session),
) -> HerdService:
    repo = HerdRepository(session)
    return HerdService(repo)
