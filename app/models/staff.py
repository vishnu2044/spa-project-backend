import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class DayOfWeek(str, enum.Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"

class Staff(Base):
    __tablename__ = "staff"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    experience_years = Column(Integer, default=0)
    bio = Column(String)
    image_url = Column(String)
    working_hours = Column(String)
    is_active = Column(Boolean, default=True)
    rating_cache = Column(Float, default=0.0)
    review_count_cache = Column(Integer, default=0)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True, unique=True)

    specialties = relationship("StaffSpecialty", back_populates="staff")
    working_days = relationship("StaffWorkingDay", back_populates="staff")
    user = relationship("User", back_populates="staff_profile")


class StaffSpecialty(Base):
    __tablename__ = "staff_specialties"

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(UUID(as_uuid=True), ForeignKey("staff.id"), nullable=False)
    category = Column(String, nullable=False)

    staff = relationship("Staff", back_populates="specialties")


class StaffWorkingDay(Base):
    __tablename__ = "staff_working_days"

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(UUID(as_uuid=True), ForeignKey("staff.id"), nullable=False)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)

    staff = relationship("Staff", back_populates="working_days")
