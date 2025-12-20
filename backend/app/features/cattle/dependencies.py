from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from .repository import CattleRepository, WeightHistoryRepository
from .service import CattleService, WeightHistoryService


def get_cattle_service(
    session: Session = Depends(get_session),
) -> CattleService:
    repo = CattleRepository(session)
    return CattleService(repo)


def get_weight_history_service(
    session: Session = Depends(get_session),
) -> WeightHistoryService:
    repo = WeightHistoryRepository(session)
    return WeightHistoryService(repo)
