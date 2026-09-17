import uuid
from sqlalchemy import Column, String, Numeric, Integer, Boolean, ForeignKey, Enum, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import enum

class OfferStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Offer(Base):
    __tablename__ = "offers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    discount_label = Column(String, nullable=True)
    promo_code = Column(String, nullable=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=True)
    status = Column(Enum(OfferStatus), default=OfferStatus.active)
    has_countdown = Column(Boolean, default=False)
    end_time = Column(DateTime, nullable=True)


class Package(Base):
    __tablename__ = "packages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    tagline = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    original_price = Column(Numeric(10, 2), nullable=True)
    duration_minutes = Column(Integer, nullable=False)
    color_theme = Column(String, nullable=True)
    is_popular = Column(Boolean, default=False)
