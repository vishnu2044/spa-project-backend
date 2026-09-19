import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    customer = "customer"
    admin = "admin"
    staff = "staff"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role = Column(Enum(UserRole), default=UserRole.customer, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    points = Column(Integer, default=0)
    join_date = Column(DateTime, default=datetime.utcnow)
    membership_plan_id = Column(UUID(as_uuid=True), nullable=True) # Optional FK
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    staff_profile = relationship("Staff", back_populates="user", uselist=False)

    @property
    def staff_id(self):
        return self.staff_profile.id if self.staff_profile else None
