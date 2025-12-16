from fastapi import APIRouter, Depends, status
from typing import List
from uuid import UUID

from .schema import CattleCreate, CattleUpdate, CattleResponse
from .service import CattleService
from .dependencies import get_cattle_service


router = APIRouter(prefix="/cattle", tags=["Cattle"])

@router.post("", response_model=CattleResponse, status_code=status.HTTP_201_CREATED)
def create_cattle( data: CattleCreate, service: CattleService = Depends(get_cattle_service)):
    return service.create(data)

@router.get("/{cattle_id}", response_model=CattleResponse)
def get_cattle(cattle_id: UUID, service: CattleService = Depends(get_cattle_service)):
    return service.get_by_id(cattle_id)

@router.get("", response_model=List[CattleResponse])
def list_cattle(
    herd_id: int | None = None,
    service: CattleService = Depends(get_cattle_service),
):
    return service.list_all(herd_id=herd_id)

@router.put("/{cattle_id}", response_model=CattleResponse)
def update_cattle(cattle_id: UUID, data: CattleUpdate, service: CattleService = Depends(get_cattle_service)):
    return service.update(cattle_id, data)

@router.delete("/{cattle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cattle(
    cattle_id: UUID,
    service: CattleService = Depends(get_cattle_service),
):
    service.delete(cattle_id)


