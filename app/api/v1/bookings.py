from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
import uuid
from datetime import datetime

router = APIRouter()

@router.get("/availability")
def get_availability(
    date: str,
    staff_id: str = None,
    service_duration: int = None,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch available time slots or booked slots.
    """
    query = db.query(models.Booking).filter(
        models.Booking.booking_date == date,
        models.Booking.status != models.booking.BookingStatus.cancelled
    )
    
    if staff_id:
        query = query.filter(models.Booking.staff_id == staff_id)
        
    bookings = query.all()
    
    booked_slots = []
    for b in bookings:
        duration = b.service.duration_minutes if b.service else 60
        booked_slots.append({
            "time": b.booking_time.strftime("%H:%M:%S"),
            "duration_minutes": duration,
            "staff_id": str(b.staff_id) if b.staff_id else None
        })
        
    return {"booked_slots": booked_slots}

@router.post("", response_model=schemas.Booking)
def create_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_in: schemas.BookingCreate,
) -> Any:
    """
    Create a new booking.
    """
    booking_id = f"AURA-{datetime.now().strftime('%Y-%m%d')}-{str(uuid.uuid4())[:4].upper()}"
    
    db_obj = models.Booking(
        id=booking_id,
        customer_id=None,
        guest_name=booking_in.guest_name,
        guest_phone=booking_in.guest_phone,
        guest_email=booking_in.guest_email,
        service_id=booking_in.service_id,
        staff_id=booking_in.staff_id,
        booking_date=booking_in.booking_date,
        booking_time=booking_in.booking_time,
        total_amount=booking_in.total_amount,
        special_notes=booking_in.special_notes,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/user/{customer_id}", response_model=List[schemas.Booking])
def read_my_bookings(
    customer_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch upcoming and past bookings for a specific user (auth temporarily disabled).
    """
    bookings = db.query(models.Booking).filter(models.Booking.customer_id == customer_id).all()
    return bookings

@router.put("/{id}/cancel", response_model=schemas.Booking)
def cancel_booking(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
) -> Any:
    """
    Cancel an upcoming booking.
    """
    booking = crud.booking.get(db=db, id=id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    booking.status = models.booking.BookingStatus.cancelled
    db.commit()
    db.refresh(booking)
    return booking
