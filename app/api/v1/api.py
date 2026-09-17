from fastapi import APIRouter
from app.api.v1 import auth, users, bookings, services, staff, reviews, admin

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(staff.router, prefix="/staff", tags=["staff"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
