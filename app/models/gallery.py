import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class GalleryItem(Base):
    __tablename__ = "gallery_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=True)
    image_url = Column(String, nullable=False)
    thumbnail_url = Column(String, nullable=True)
    alt_text = Column(String, nullable=True)
    caption = Column(String, nullable=True)
    is_before_after = Column(Boolean, default=False)
    before_image_url = Column(String, nullable=True)
