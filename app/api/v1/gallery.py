from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("", response_model=List[schemas.GalleryItem])
def read_gallery(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve gallery items.
    """
    items = crud.gallery.get_multi(db, skip=skip, limit=limit)
    return items

@router.post("", response_model=schemas.GalleryItem)
def create_gallery_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.GalleryItemCreate,
) -> Any:
    """
    Create new gallery item (Admin only).
    """
    item = crud.gallery.create(db, obj_in=item_in)
    return item
