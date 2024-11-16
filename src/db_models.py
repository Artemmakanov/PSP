from sqlalchemy import create_engine, MetaData, UniqueConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from .config import conf
from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    login = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    __table_args__ = (UniqueConstraint('login'), )

class Papers(db.Model):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link_ru = Column(String)
    link_en = Column(String)
    filepath = Column(String, nullable=False)
    __table_args__ = (UniqueConstraint('title', 'link_ru', 'link_en', 'filepath'), )

class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    paper_id = mapped_column(Integer, ForeignKey("papers.id"))