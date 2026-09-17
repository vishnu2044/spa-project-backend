from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from app.models.staff import DayOfWeek

class StaffSpecialtyBase(BaseModel):
    category: str

class StaffSpecialtyCreate(StaffSpecialtyBase):
    pass

class StaffSpecialty(StaffSpecialtyBase):
    id: int
    staff_id: UUID

    class Config:
        from_attributes = True

class StaffWorkingDayBase(BaseModel):
    day_of_week: DayOfWeek

class StaffWorkingDayCreate(StaffWorkingDayBase):
    pass

class StaffWorkingDay(StaffWorkingDayBase):
    id: int
    staff_id: UUID

    class Config:
        from_attributes = True

class StaffBase(BaseModel):
    name: str
    role: str
    experience_years: Optional[int] = 0
    bio: Optional[str] = None
    image_url: Optional[str] = None
    working_hours: Optional[str] = None
    is_active: Optional[bool] = True

class StaffCreate(StaffBase):
    pass

class StaffUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None
    image_url: Optional[str] = None
    working_hours: Optional[str] = None
    is_active: Optional[bool] = None

class Staff(StaffBase):
    id: UUID
    rating_cache: float
    review_count_cache: int
    specialties: List[StaffSpecialty] = []
    working_days: List[StaffWorkingDay] = []

    class Config:
        from_attributes = True
