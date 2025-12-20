from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone

import pytest
from fastapi import HTTPException
from unittest.mock import Mock

from app.features.cattle.service import CattleService, WeightHistoryService
from app.features.cattle.model import Cattle, WeightHistory
from app.features.cattle.schema import CattleCreate, CattleRead, CattleUpdate
from app.features.cattle.repository import (
    CattleRepository,
    WeightHistoryRepository,
)

# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def cattle_repository() -> Mock:
    return Mock(spec=CattleRepository)


@pytest.fixture
def cattle_service(cattle_repository: Mock) -> CattleService:
    return CattleService(repository=cattle_repository)


@pytest.fixture
def weight_history_repository() -> Mock:
    return Mock(spec=WeightHistoryRepository)


@pytest.fixture
def weight_history_service(
    weight_history_repository: Mock,
) -> WeightHistoryService:
    return WeightHistoryService(repository=weight_history_repository)


# ============================================================================
# Helpers to create real objects
# ============================================================================


def make_cattle(
    id: Optional[UUID] = None,
    identifier: str = "ABC123",
) -> Cattle:
    return Cattle(
        id=id or uuid4(),
        identifier=identifier,
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc),
        deleted_at=None,
    )


def make_weight_history(
    cattle_id: Optional[UUID] = None,
    id: Optional[UUID] = None,
    weight: float = 350.0,
) -> WeightHistory:
    return WeightHistory(
        id=id or uuid4(),
        cattle_id=cattle_id or uuid4(),
        weight=weight,
        measured_at=datetime.now(tz=timezone.utc),
    )


# ============================================================================
# CattleService tests
# ============================================================================


def test_create_cattle_success(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    data = CattleCreate(identifier="ABC123")
    cattle = make_cattle()

    cattle_repository.get_by_identifier.return_value = None
    cattle_repository.create.return_value = cattle

    result = cattle_service.create(data)

    assert result is cattle
    cattle_repository.get_by_identifier.assert_called_once_with("ABC123")
    cattle_repository.create.assert_called_once_with(data)


def test_create_cattle_duplicate_identifier_raises(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    data = CattleCreate(identifier="ABC123")
    cattle_repository.get_by_identifier.return_value = make_cattle()

    with pytest.raises(HTTPException) as exc:
        cattle_service.create(data)

    assert exc.value.status_code == 400
    assert "already exists" in exc.value.detail


def test_get_all_cattle(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_repository.get_all.return_value = [make_cattle(), make_cattle()]

    result = cattle_service.get_all()

    assert len(result) == 2
    assert all(isinstance(c, CattleRead) for c in result)
    cattle_repository.get_all.assert_called_once_with(herd_id=None)


def test_get_cattle_by_id_success(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_id = uuid4()
    cattle_repository.get_by_id.return_value = make_cattle(cattle_id)

    result = cattle_service.get_by_id(cattle_id)

    assert isinstance(result, CattleRead)
    cattle_repository.get_by_id.assert_called_once_with(cattle_id)


def test_get_cattle_by_id_not_found(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_repository.get_by_id.return_value = None

    with pytest.raises(HTTPException) as exc:
        cattle_service.get_by_id(uuid4())

    assert exc.value.status_code == 404


def test_update_cattle_success(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_id = uuid4()
    cattle = make_cattle(cattle_id)
    updated = make_cattle(cattle_id, identifier="NEWID")

    cattle_repository.get_by_id.return_value = cattle
    cattle_repository.update.return_value = updated

    result = cattle_service.update(cattle_id, CattleUpdate(identifier="NEWID"))

    assert isinstance(result, CattleRead)
    assert result.identifier == "NEWID"
    cattle_repository.update.assert_called_once_with(
        cattle, CattleUpdate(identifier="NEWID")
    )


def test_update_cattle_not_found(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_repository.get_by_id.return_value = None

    with pytest.raises(HTTPException) as exc:
        cattle_service.update(uuid4(), CattleUpdate(identifier="NEWID"))

    assert exc.value.status_code == 404


def test_delete_cattle_success(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle = make_cattle()
    cattle_repository.get_by_id.return_value = cattle

    cattle_service.delete(cattle.id)

    cattle_repository.delete.assert_called_once_with(cattle)


def test_delete_cattle_not_found(
    cattle_service: CattleService,
    cattle_repository: Mock,
) -> None:
    cattle_repository.get_by_id.return_value = None

    with pytest.raises(HTTPException) as exc:
        cattle_service.delete(uuid4())

    assert exc.value.status_code == 404


# ============================================================================
# WeightHistoryService tests
# ============================================================================


def test_create_weight_history(
    weight_history_service: WeightHistoryService,
    weight_history_repository: Mock,
) -> None:
    cattle_id = uuid4()
    record = make_weight_history(cattle_id=cattle_id)

    weight_history_repository.create.return_value = record

    result = weight_history_service.create(
        cattle_id=cattle_id,
        weight=350.5,
        measured_at=datetime.now(tz=timezone.utc),
    )

    assert result is record


def test_get_all_weight_history(
    weight_history_service: WeightHistoryService,
    weight_history_repository: Mock,
) -> None:
    records = [make_weight_history(), make_weight_history()]
    weight_history_repository.get_all.return_value = records

    result = weight_history_service.get_all(uuid4())

    assert result == records


def test_delete_weight_history_success(
    weight_history_service: WeightHistoryService,
    weight_history_repository: Mock,
) -> None:
    record = make_weight_history()
    weight_history_repository.get_by_id.return_value = record

    weight_history_service.delete(uuid4(), record.id)

    weight_history_repository.delete.assert_called_once_with(record)


def test_delete_weight_history_not_found(
    weight_history_service: WeightHistoryService,
    weight_history_repository: Mock,
) -> None:
    weight_history_repository.get_by_id.return_value = None

    with pytest.raises(HTTPException) as exc:
        weight_history_service.delete(uuid4(), uuid4())

    assert exc.value.status_code == 404
