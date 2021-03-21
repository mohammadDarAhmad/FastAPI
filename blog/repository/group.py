from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Group, db: Session):
    new_group = models.Group(
        name=request.name, description=request.email)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group


def show(id: int, db: Session):
    group = db.query(models.Group).filter(models.Group.id == id).first()
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"group with the id {id} is not available")
    return group