from . import schemas, models, database
from .database import engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status , HTTPException


app = FastAPI()


models.Base.metadata.create_all(engine)


get_db = database.get_db


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), ):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}',  status_code=status.HTTP_204_NO_CONTENT )
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This is not available")
    return blog
