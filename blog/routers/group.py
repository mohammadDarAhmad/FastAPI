from blog import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from blog.repository import  group

router = APIRouter(
    prefix="/group",
    tags=['Groups']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowGroup)
def creat_group(request: schemas.User, db: Session = Depends(get_db)):
    return group.create(request, db)


@router.get('/{id}', response_model=schemas.ShowGroup)
def get_group(id: int, db: Session = Depends(get_db)):
    return group.show(id, db)