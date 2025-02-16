from sqlalchemy import create_engine, MetaData, UniqueConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from .config import conf
from . import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    login = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    __table_args__ = (UniqueConstraint('login'), )

class Papers(Base):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    stems = Column(String, nullable=False)
    link_ru = Column(String)
    link_en = Column(String)
    filepath = Column(String, nullable=False)
    __table_args__ = (UniqueConstraint('title', 'link_ru', 'link_en', 'filepath'), )

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    paper_id = mapped_column(Integer, ForeignKey("papers.id"))