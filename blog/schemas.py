from typing import List, Optional, Tuple

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class Group(BaseModel):
    name: str
    description: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowUserGroup(BaseModel):
    users: ShowUser

    class Config():
        orm_mode = True


class ShowGroup(BaseModel):
    name: str
    description: str
    group_user: List[ShowUserGroup] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
