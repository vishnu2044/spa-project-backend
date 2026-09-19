from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID
from datetime import date, time, datetime
from app.models.booking import BookingStatus
from app.schemas.service import Service
from app.schemas.staff import Staff

class BookingBase(BaseModel):
    guest_name: Optional[str] = Field(None, min_length=2, max_length=50)
    guest_phone: Optional[str] = Field(None, min_length=10, max_length=15)
    guest_email: Optional[EmailStr] = None
    service_id: UUID
    staff_id: Optional[UUID] = None
    booking_date: date
    booking_time: time
    total_amount: Optional[float] = Field(0.0, ge=0)
    special_notes: Optional[str] = Field(None, max_length=500)

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
    service: Optional[Service] = None
    staff: Optional[Staff] = None

    class Config:
        from_attributes = True
