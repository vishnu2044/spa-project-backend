import uuid
from sqlalchemy import Column, String, Numeric, DateTime, Date, Time, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import datetime

class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"

class Booking(Base):
    __tablename__ = "bookings"

    # Custom format e.g., 'AURA-2026-0917-1001'
    id = Column(String, primary_key=True)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    guest_name = Column(String, nullable=True)
    guest_phone = Column(String, nullable=True)
    guest_email = Column(String, nullable=True)
    
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    staff_id = Column(UUID(as_uuid=True), ForeignKey("staff.id"), nullable=True)
    
    booking_date = Column(Date, nullable=False)
    booking_time = Column(Time, nullable=False)
    status = Column(Enum(BookingStatus), default=BookingStatus.pending)
    total_amount = Column(Numeric(10, 2), nullable=False)
    special_notes = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    customer = relationship("User")
    service = relationship("Service")
    staff = relationship("Staff")
