from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .database import Base
from sqlalchemy.orm import relationship, backref


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs_user")


class userGroup(Base):
    __tablename__ ='userGroup'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    users = relationship("User", back_populates="user_group")
    groups = relationship("Group", back_populates="group_user")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs_user = relationship('Blog', back_populates="creator")
    user_group = relationship("userGroup", back_populates="users")


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    group_user = relationship("userGroup", back_populates="groups")
