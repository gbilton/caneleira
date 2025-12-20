from fastapi import APIRouter, Depends, status
from typing import List, Optional
from uuid import UUID

from .schema import (
    CattleCreate,
    CattleUpdate,
    CattleResponse,
    WeightHistoryCreate,
    WeightHistoryResponse,
)
from .service import CattleService, WeightHistoryService
from .dependencies import get_cattle_service, get_weight_history_service


router = APIRouter(prefix="/cattle", tags=["Cattle"])

# Cattle endpoints


@router.post(
    "", response_model=CattleResponse, status_code=status.HTTP_201_CREATED
)
def create_cattle(
    data: CattleCreate, service: CattleService = Depends(get_cattle_service)
):
    return service.create(data)


@router.get("", response_model=List[CattleResponse])
def list_cattle(
    herd_id: Optional[UUID] = None,
    service: CattleService = Depends(get_cattle_service),
):
    return service.get_all(herd_id=herd_id)


@router.get("/{cattle_id}", response_model=CattleResponse)
def get_cattle(
    cattle_id: UUID, service: CattleService = Depends(get_cattle_service)
):
    return service.get_by_id(cattle_id)


@router.put("/{cattle_id}", response_model=CattleResponse)
def update_cattle(
    cattle_id: UUID,
    data: CattleUpdate,
    service: CattleService = Depends(get_cattle_service),
):
    return service.update(cattle_id, data)


@router.delete("/{cattle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cattle(
    cattle_id: UUID,
    service: CattleService = Depends(get_cattle_service),
):
    service.delete(cattle_id)


# Weight history endpoints


@router.post(
    "/{cattle_id}/weight-history",
    response_model=WeightHistoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_weight_history_record(
    data: WeightHistoryCreate,
    service: WeightHistoryService = Depends(get_weight_history_service),
):
    return service.create(data.cattle_id, data.weight, data.measured_at)


@router.get(
    "/{cattle_id}/weight-history", response_model=List[WeightHistoryResponse]
)
def get_weight_history(
    cattle_id: UUID,
    service: WeightHistoryService = Depends(get_weight_history_service),
):
    return service.get_all(cattle_id)


@router.delete(
    "/{cattle_id}/weight-history/{weight_history_record_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_weight_history(
    cattle_id: UUID,
    weight_history_record_id: UUID,
    service: WeightHistoryService = Depends(get_weight_history_service),
):
    service.delete(cattle_id, weight_history_record_id)
