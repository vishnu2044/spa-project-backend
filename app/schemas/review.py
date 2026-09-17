from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.review import ReviewStatus

class ReviewBase(BaseModel):
    booking_id: Optional[str] = None
    service_id: UUID
    rating: int
    text: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    status: Optional[ReviewStatus] = None

class Review(ReviewBase):
    id: UUID
    customer_id: UUID
    is_verified: bool
    status: ReviewStatus
    created_at: datetime

    class Config:
        from_attributes = True
