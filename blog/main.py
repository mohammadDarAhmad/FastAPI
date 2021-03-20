from . import schemas, models, database
from .database import engine
from blog.routers import blog, user
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, HTTPException

app = FastAPI(
    title="FastAPI project",
    description="Small project to learn FastAPI framework",
    version="1.0.0"
)

models.Base.metadata.create_all(engine)

get_db = database.get_db

app.include_router(blog.router)
app.include_router(user.router)
