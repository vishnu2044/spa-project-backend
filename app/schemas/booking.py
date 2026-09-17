from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import date, time, datetime
from app.models.booking import BookingStatus

class BookingBase(BaseModel):
    guest_name: Optional[str] = None
    guest_phone: Optional[str] = None
    guest_email: Optional[EmailStr] = None
    service_id: UUID
    staff_id: Optional[UUID] = None
    booking_date: date
    booking_time: time
    total_amount: float
    special_notes: Optional[str] = None

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    status: Optional[BookingStatus] = None

class Booking(BookingBase):
    id: str
    customer_id: Optional[UUID] = None
    status: BookingStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
