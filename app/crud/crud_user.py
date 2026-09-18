from typing import Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user import User, UserRole
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_phone(self, db: Session, *, phone: str) -> Optional[User]:
        return db.query(User).filter(User.phone == phone).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            phone=obj_in.phone,
            name=obj_in.name,
            password_hash=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def make_admin(self, db: Session, *, user_id: str) -> Optional[User]:
        db_obj = self.get(db, id=user_id)
        if db_obj:
            db_obj.role = UserRole.admin
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def toggle_block(self, db: Session, *, user_id: str, block: bool) -> Optional[User]:
        db_obj = self.get(db, id=user_id)
        if db_obj:
            db_obj.is_active = not block
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return db_obj

user = CRUDUser(User)
