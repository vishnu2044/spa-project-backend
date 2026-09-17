from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("", response_model=List[schemas.Review])
def read_reviews(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve published reviews.
    """
    # Should ideally filter by status='published'
    reviews = crud.review.get_multi(db, skip=skip, limit=limit)
    return [r for r in reviews if r.status == models.review.ReviewStatus.published]

@router.post("", response_model=schemas.Review)
def create_review(
    *,
    db: Session = Depends(deps.get_db),
    review_in: schemas.ReviewCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Submit a new review.
    """
    review = crud.review.create(db, obj_in=review_in)
    review.customer_id = current_user.id
    db.commit()
    db.refresh(review)
    return review
