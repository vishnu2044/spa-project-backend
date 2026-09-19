from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("", response_model=List[schemas.Offer])
def read_offers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve active offers.
    """
    offers = crud.offer.get_multi(db, skip=skip, limit=limit)
    return [o for o in offers if o.status == models.offer.OfferStatus.active]

@router.post("", response_model=schemas.Offer)
def create_offer(
    *,
    db: Session = Depends(deps.get_db),
    offer_in: schemas.OfferCreate,
) -> Any:
    """
    Create new offer (Admin only).
    """
    offer = crud.offer.create(db, obj_in=offer_in)
    return offer

@router.put("/{id}", response_model=schemas.Offer)
def update_offer(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    offer_in: schemas.OfferUpdate,
) -> Any:
    """
    Update an offer.
    """
    offer = crud.offer.get(db=db, id=id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    offer = crud.offer.update(db=db, db_obj=offer, obj_in=offer_in)
    return offer
