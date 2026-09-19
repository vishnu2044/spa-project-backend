from sqlalchemy import text
from app.core.database import SessionLocal, engine
from app.models.offer import Package, Offer
from app.models.gallery import GalleryItem
from app.models.staff import Staff
from app.models.user import User

def migrate():
    print("Creating new tables...")
    Package.__table__.create(engine, checkfirst=True)
    Offer.__table__.create(engine, checkfirst=True)
    GalleryItem.__table__.create(engine, checkfirst=True)

    db = SessionLocal()
    
    print("Altering staff table...")
    try:
        db.execute(text("ALTER TABLE staff ADD COLUMN user_id UUID REFERENCES users(id);"))
        db.commit()
        print("Successfully added user_id to staff table.")
    except Exception as e:
        db.rollback()
        print(f"Notice (staff user_id): {e}")

    print("Altering userrole enum...")
    try:
        db.execute(text("ALTER TYPE userrole ADD VALUE 'staff';"))
        db.commit()
        print("Successfully added 'staff' to userrole enum.")
    except Exception as e:
        db.rollback()
        print(f"Notice (userrole enum): {e}")

    db.close()

if __name__ == "__main__":
    migrate()
