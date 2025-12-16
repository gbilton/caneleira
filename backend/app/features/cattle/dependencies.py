from fastapi import Depends
from app.db.session import get_session
from .repository import CattleRepository
from .service import CattleService


def get_cattle_service(
    session = Depends(get_session),
) -> CattleService:
    repo = CattleRepository(session)
    return CattleService(repo)
