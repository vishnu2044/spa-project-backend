import uuid
from sqlalchemy import Column, String, Integer, Numeric, Boolean, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class ServiceStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True, nullable=False)

    services = relationship("Service", back_populates="category")


class Service(Base):
    __tablename__ = "services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)
    name = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String)
    description = Column(Text)
    before_care_instructions = Column(Text)
    is_popular = Column(Boolean, default=False)
    status = Column(Enum(ServiceStatus), default=ServiceStatus.active)

    category = relationship("Category", back_populates="services")
