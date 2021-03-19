from fastapi import FastAPI
from . import schemas, models,database
from .database import engine
from sqlalchemy.orm import Session
from fastapi import Depends


app = FastAPI()


models.Base.metadata.create_all(engine)


get_db = database.get_db


@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
