from typing import List
from blog import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from blog.repository import  group

router = APIRouter(
    prefix="/group",
    tags=['Groups']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowGroup])
def all(db: Session = Depends(get_db)):
    return group.get_all(db)


@router.post('/', response_model=schemas.ShowGroup)
def creat_group(request: schemas.Group, db: Session = Depends(get_db)):
    return group.create(request, db)


@router.get('/{id}', response_model=schemas.ShowGroup)
def get_group(id: int, db: Session = Depends(get_db)):
    return group.show(id, db)


@router.post('/{id_group}/addUserToGroup', response_model=schemas.ShowGroup)
def add_user(id_group: int, id_user: int, db: Session = Depends(get_db)):
    return group.add_user(id_group, id_user, db)

