from sqlalchemy.orm import Session

from app.features.cattle.repository import CattleRepository
from app.features.cattle.schema import CattleCreate


def test_create_cattle(db: Session):
    repo = CattleRepository(db)

    cattle = repo.create(
        CattleCreate(
            identifier="Bessie",
        )
    )

    assert cattle.id is not None
    assert cattle.identifier == "Bessie"
