from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id > 0:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id not found"}


class Blog(BaseModel):
    pass


@app.post("/blog")
def create_blog():
    return {"data":"Blog is created"}
