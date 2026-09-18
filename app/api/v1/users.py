from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
import uuid

router = APIRouter()

@router.get("", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve all users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get current user (auth disabled, returning first user as dummy).
    """
    users = crud.user.get_multi(db, limit=1)
    if not users:
        raise HTTPException(status_code=404, detail="No users exist in the database")
    return users[0]

@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user (auth temporarily disabled).
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a specific user (auth temporarily disabled).
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user

@router.get("/{user_id}/rewards")
def read_user_rewards(
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get user rewards (auth temporarily disabled).
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"points": user.points}

@router.put("/{user_id}/make-admin", response_model=schemas.User)
def make_user_admin(
    *,
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Elevate a user to admin role.
    """
    user = crud.user.make_admin(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}/block", response_model=schemas.User)
def block_user(
    *,
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Block a user from using the platform.
    """
    user = crud.user.toggle_block(db, user_id=user_id, block=True)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}/unblock", response_model=schemas.User)
def unblock_user(
    *,
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Unblock a user.
    """
    user = crud.user.toggle_block(db, user_id=user_id, block=False)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
