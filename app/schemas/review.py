from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.review import ReviewStatus

class ReviewCustomer(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True

class ReviewBase(BaseModel):
    booking_id: Optional[str] = None
    service_id: UUID
    rating: int = Field(ge=1, le=5)
    text: Optional[str] = Field(None, max_length=1000)

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
    customer: Optional[ReviewCustomer] = None

    class Config:
        from_attributes = True
