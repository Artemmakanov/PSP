from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from .config import conf
from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    login = Column(String)
    password_hash = Column(String)

class Papers(db.Model):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link_ru = Column(String)
    link_en = Column(String)
    filepath = Column(String)

class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    paper_id = mapped_column(Integer, ForeignKey("papers.id"))