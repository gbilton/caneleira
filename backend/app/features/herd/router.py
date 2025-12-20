from fastapi import APIRouter, Depends, status
from typing import List
from uuid import UUID

from .schema import HerdCreate, HerdUpdate, HerdResponse
from .service import HerdService
from .dependencies import get_herd_service


router = APIRouter(prefix="/herd", tags=["Herd"])


@router.post(
    "", response_model=HerdResponse, status_code=status.HTTP_201_CREATED
)
def create_herd(
    data: HerdCreate, service: HerdService = Depends(get_herd_service)
):
    return service.create(data)


@router.get("/{herd_id}", response_model=HerdResponse)
def get_herd(herd_id: UUID, service: HerdService = Depends(get_herd_service)):
    return service.get_by_id(herd_id)


@router.get("", response_model=List[HerdResponse])
def list_herds(service: HerdService = Depends(get_herd_service)):
    return service.list_all()


@router.put("/{herd_id}", response_model=HerdResponse)
def update_herd(
    herd_id: UUID,
    data: HerdUpdate,
    service: HerdService = Depends(get_herd_service),
):
    return service.update(herd_id, data)


@router.delete("/{herd_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_herd(
    herd_id: UUID,
    service: HerdService = Depends(get_herd_service),
):
    service.delete(herd_id)
