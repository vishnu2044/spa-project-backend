import uuid
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import datetime

class ReviewStatus(str, enum.Enum):
    published = "published"
    hidden = "hidden"

class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    booking_id = Column(String, ForeignKey("bookings.id"), nullable=True)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    
    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=True)
    is_verified = Column(Boolean, default=False)
    status = Column(Enum(ReviewStatus), default=ReviewStatus.published)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("User")
