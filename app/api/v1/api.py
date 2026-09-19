from fastapi import APIRouter
from app.api.v1 import auth, users, bookings, services, staff, reviews, admin, offers, packages, gallery

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(staff.router, prefix="/staff", tags=["staff"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(offers.router, prefix="/offers", tags=["offers"])
api_router.include_router(packages.router, prefix="/packages", tags=["packages"])
api_router.include_router(gallery.router, prefix="/gallery", tags=["gallery"])
