from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.offer import OfferStatus

class OfferBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    discount_label: Optional[str] = None
    promo_code: Optional[str] = None
    category_id: Optional[UUID] = None
    status: Optional[OfferStatus] = OfferStatus.active
    has_countdown: Optional[bool] = False
    end_time: Optional[datetime] = None

class OfferCreate(OfferBase):
    pass

class OfferUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    discount_label: Optional[str] = None
    promo_code: Optional[str] = None
    category_id: Optional[UUID] = None
    status: Optional[OfferStatus] = None
    has_countdown: Optional[bool] = None
    end_time: Optional[datetime] = None

class Offer(OfferBase):
    id: UUID

    class Config:
        from_attributes = True

class PackageBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    tagline: Optional[str] = None
    description: Optional[str] = None
    price: float = Field(ge=0)
    original_price: Optional[float] = None
    duration_minutes: int
    color_theme: Optional[str] = None
    is_popular: Optional[bool] = False

class PackageCreate(PackageBase):
    pass

class PackageUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    tagline: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    original_price: Optional[float] = None
    duration_minutes: Optional[int] = None
    color_theme: Optional[str] = None
    is_popular: Optional[bool] = None

class Package(PackageBase):
    id: UUID

    class Config:
        from_attributes = True
