from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("", response_model=List[schemas.Package])
def read_packages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve packages.
    """
    packages = crud.package.get_multi(db, skip=skip, limit=limit)
    return packages

@router.post("", response_model=schemas.Package)
def create_package(
    *,
    db: Session = Depends(deps.get_db),
    package_in: schemas.PackageCreate,
) -> Any:
    """
    Create new package (Admin only).
    """
    package = crud.package.create(db, obj_in=package_in)
    return package
