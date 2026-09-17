from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from app.models.service import ServiceStatus

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: UUID

    class Config:
        from_attributes = True

class ServiceBase(BaseModel):
    name: str
    duration_minutes: int
    price: float
    image_url: Optional[str] = None
    description: Optional[str] = None
    before_care_instructions: Optional[str] = None
    is_popular: Optional[bool] = False
    status: Optional[ServiceStatus] = ServiceStatus.active
    category_id: UUID

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    duration_minutes: Optional[int] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    before_care_instructions: Optional[str] = None
    is_popular: Optional[bool] = None
    status: Optional[ServiceStatus] = None
    category_id: Optional[UUID] = None

class Service(ServiceBase):
    id: UUID

    class Config:
        from_attributes = True
