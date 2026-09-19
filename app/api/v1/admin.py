from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/dashboard/stats")
def get_dashboard_stats(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get daily revenue, pending/completed appointments counts.
    """
    return {"message": "Stats to be implemented"}

@router.get("/bookings", response_model=List[schemas.Booking])
def get_all_bookings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.booking.get_multi(db, skip=skip, limit=limit)

@router.delete("/bookings/{id}")
def delete_booking(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
) -> Any:
    booking = crud.booking.get(db=db, id=id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking = crud.booking.remove(db=db, id=id)
    return {"status": "success", "message": "Booking deleted"}

@router.post("/services", response_model=schemas.Service)
def create_service(
    *,
    db: Session = Depends(deps.get_db),
    service_in: schemas.ServiceCreate,
) -> Any:
    service = crud.service.create(db, obj_in=service_in)
    return service

@router.put("/services/{id}", response_model=schemas.Service)
def update_service(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    service_in: schemas.ServiceUpdate,
) -> Any:
    service = crud.service.get(db=db, id=id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    service = crud.service.update(db=db, db_obj=service, obj_in=service_in)
    return service

@router.delete("/services/{id}")
def delete_service(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
) -> Any:
    service = crud.service.get(db=db, id=id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    service = crud.service.remove(db=db, id=id)
    return {"status": "success", "message": "Service deleted"}

@router.get("/staff", response_model=List[schemas.Staff])
def get_all_staff(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.staff.get_multi(db, skip=skip, limit=limit)

@router.post("/staff", response_model=schemas.Staff)
def create_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_in: schemas.StaffCreate,
) -> Any:
    staff = crud.staff.create(db, obj_in=staff_in)
    return staff

@router.put("/staff/{id}", response_model=schemas.Staff)
def update_staff(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    staff_in: schemas.StaffUpdate,
) -> Any:
    staff = crud.staff.get(db=db, id=id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    staff = crud.staff.update(db=db, db_obj=staff, obj_in=staff_in)
    return staff

@router.delete("/staff/{id}")
def delete_staff(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
) -> Any:
    staff = crud.staff.get(db=db, id=id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    staff = crud.staff.remove(db=db, id=id)
    return {"status": "success", "message": "Staff deleted"}
