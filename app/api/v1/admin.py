from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/dashboard/stats")
def get_dashboard_stats(
    db: Session = Depends(deps.get_db),
    current_admin: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Get daily revenue, pending/completed appointments counts.
    """
    return {"message": "Stats to be implemented"}

@router.get("/bookings", response_model=List[schemas.Booking])
def get_all_bookings(
    db: Session = Depends(deps.get_db),
    current_admin: models.User = Depends(deps.get_current_active_admin),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.booking.get_multi(db, skip=skip, limit=limit)

@router.post("/services", response_model=schemas.Service)
def create_service(
    *,
    db: Session = Depends(deps.get_db),
    service_in: schemas.ServiceCreate,
    current_admin: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    service = crud.service.create(db, obj_in=service_in)
    return service

@router.post("/staff", response_model=schemas.Staff)
def create_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_in: schemas.StaffCreate,
    current_admin: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    staff = crud.staff.create(db, obj_in=staff_in)
    return staff
