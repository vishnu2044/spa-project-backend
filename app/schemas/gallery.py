from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class GalleryItemBase(BaseModel):
    category_id: Optional[UUID] = None
    image_url: str
    thumbnail_url: Optional[str] = None
    alt_text: Optional[str] = None
    caption: Optional[str] = None
    is_before_after: Optional[bool] = False
    before_image_url: Optional[str] = None

class GalleryItemCreate(GalleryItemBase):
    pass

class GalleryItemUpdate(BaseModel):
    category_id: Optional[UUID] = None
    image_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    alt_text: Optional[str] = None
    caption: Optional[str] = None
    is_before_after: Optional[bool] = None
    before_image_url: Optional[str] = None

class GalleryItem(GalleryItemBase):
    id: UUID

    class Config:
        from_attributes = True
