import uuid
from app.core.database import SessionLocal, engine
from app.models import Base
from app.models.service import Category, Service
from app.models.staff import Staff, StaffSpecialty

# Create tables just in case
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    try:
        # Check if we already have a category
        existing_category = db.query(Category).filter(Category.name == "Hair").first()
        if not existing_category:
            print("Seeding Category...")
            category = Category(
                id=uuid.uuid4(),
                name="Hair"
            )
            db.add(category)
            db.commit()
            db.refresh(category)
        else:
            print("Category already exists.")
            category = existing_category

        # Check if we already have a service
        existing_service = db.query(Service).filter(Service.name == "Classic Haircut").first()
        if not existing_service:
            print("Seeding Service...")
            service = Service(
                id=uuid.uuid4(),
                category_id=category.id,
                name="Classic Haircut",
                duration_minutes=45,
                price=50.00,
                description="A timeless classic haircut by our top professionals.",
                is_popular=True
            )
            db.add(service)
            db.commit()
        else:
            print("Service already exists.")

        # Check if we already have a staff member
        existing_staff = db.query(Staff).filter(Staff.name == "Sarah Jenkins").first()
        if not existing_staff:
            print("Seeding Staff...")
            staff = Staff(
                id=uuid.uuid4(),
                name="Sarah Jenkins",
                role="Senior Stylist",
                experience_years=8,
                bio="Sarah is a senior stylist with 8 years of experience."
            )
            db.add(staff)
            db.commit()
            db.refresh(staff)

            print("Seeding Staff Specialty...")
            specialty = StaffSpecialty(
                staff_id=staff.id,
                category="Hair"
            )
            db.add(specialty)
            db.commit()
        else:
            print("Staff member already exists.")

        print("Seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
