from .crud_user import user
from app.crud.base import CRUDBase
from app.models.staff import Staff
from app.models.service import Service, Category
from app.models.booking import Booking
from app.models.review import Review
from app.models.offer import Offer, Package
from app.models.gallery import GalleryItem
from app.schemas.staff import StaffCreate, StaffUpdate
from app.schemas.service import ServiceCreate, ServiceUpdate, CategoryCreate
from app.schemas.booking import BookingCreate, BookingUpdate
from app.schemas.review import ReviewCreate, ReviewUpdate
from app.schemas.offer import OfferCreate, OfferUpdate, PackageCreate, PackageUpdate
from app.schemas.gallery import GalleryItemCreate, GalleryItemUpdate

staff = CRUDBase[Staff, StaffCreate, StaffUpdate](Staff)
service = CRUDBase[Service, ServiceCreate, ServiceUpdate](Service)
category = CRUDBase[Category, CategoryCreate, CategoryCreate](Category)
booking = CRUDBase[Booking, BookingCreate, BookingUpdate](Booking)
review = CRUDBase[Review, ReviewCreate, ReviewUpdate](Review)
offer = CRUDBase[Offer, OfferCreate, OfferUpdate](Offer)
package = CRUDBase[Package, PackageCreate, PackageUpdate](Package)
gallery = CRUDBase[GalleryItem, GalleryItemCreate, GalleryItemUpdate](GalleryItem)
