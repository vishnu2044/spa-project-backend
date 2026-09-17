from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.offer import OfferStatus

class OfferBase(BaseModel):
    title: str
    description: Optional[str] = None
    discount_label: Optional[str] = None
    promo_code: Optional[str] = None
    category_id: Optional[UUID] = None
    status: Optional[OfferStatus] = OfferStatus.active
    has_countdown: Optional[bool] = False
    end_time: Optional[datetime] = None

class OfferCreate(OfferBase):
    pass

class OfferUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
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
    name: str
    tagline: Optional[str] = None
    description: Optional[str] = None
    price: float
    original_price: Optional[float] = None
    duration_minutes: int
    color_theme: Optional[str] = None
    is_popular: Optional[bool] = False

class PackageCreate(PackageBase):
    pass

class PackageUpdate(BaseModel):
    name: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    original_price: Optional[float] = None
    duration_minutes: Optional[int] = None
    color_theme: Optional[str] = None
    is_popular: Optional[bool] = None

class Package(PackageBase):
    id: UUID

    class Config:
        from_attributes = True
