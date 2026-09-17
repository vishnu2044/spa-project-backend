from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("", response_model=List[schemas.Staff])
def read_staff(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve staff.
    """
    staff_members = crud.staff.get_multi(db, skip=skip, limit=limit)
    return staff_members

@router.get("/{id}", response_model=schemas.Staff)
def read_staff_by_id(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get specific staff details.
    """
    staff_member = crud.staff.get(db=db, id=id)
    return staff_member
