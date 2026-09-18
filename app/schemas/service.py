from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from app.models.service import ServiceStatus

class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: UUID

    class Config:
        from_attributes = True

class ServiceBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    duration_minutes: int = Field(gt=0)
    price: float = Field(ge=0)
    image_url: Optional[str] = None
    description: Optional[str] = Field(None, max_length=1000)
    before_care_instructions: Optional[str] = None
    is_popular: Optional[bool] = False
    status: Optional[ServiceStatus] = ServiceStatus.active
    category_id: UUID

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    duration_minutes: Optional[int] = Field(None, gt=0)
    price: Optional[float] = Field(None, ge=0)
    image_url: Optional[str] = None
    description: Optional[str] = Field(None, max_length=1000)
    before_care_instructions: Optional[str] = None
    is_popular: Optional[bool] = None
    status: Optional[ServiceStatus] = None
    category_id: Optional[UUID] = None

class Service(ServiceBase):
    id: UUID

    class Config:
        from_attributes = True
