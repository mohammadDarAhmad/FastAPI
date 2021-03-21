from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Group, db: Session):
    new_group = models.Group(
        name=request.name, description=request.description)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group


def get_all(db: Session):
    groups = db.query(models.Group).all()
    return groups


# This method to print all user have a group
def get_users_have_group(db: Session):
    users = db.query(models.User).join(models.userGroup).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="not available any user in group")
    return users


def show(id: int, db: Session):
    group = db.query(models.Group).filter(models.Group.id == id).first()
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"group with the id {id} is not available")
    return group


def add_user(id_group: int, id_user: int, db: Session):
    group = db.query(models.Group).filter(models.Group.id == id_group).first()
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="This group is not available")
    user = db.query(models.User).filter(models.User.id == id_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="This user is not available")
    user_group = models.userGroup()
    user_group.user_id = id_user
    user_group.group_id = id_group

    db.add(user_group)
    db.commit()
    return group
