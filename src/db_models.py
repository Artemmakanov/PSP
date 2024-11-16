from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from config import conf
engine = create_engine(conf.postgres_url)
meta = MetaData()


users = Table(
    conf.postgres_table_users, meta, 
    Column('id', Integer, primary_key = True), 
    Column('name', String), 
    Column('surname', String),
    Column('patronymic', String),
    Column('login', String),
    Column('password_hash', String),
)

papers = Table(
    conf.postgres_table_papers, meta, 
    Column('id', Integer, primary_key = True), 
    Column('title', String), 
    Column('link_ru', String),
    Column('link_en', String),
    Column('filepath', String),
)

views = Table(
    conf.postgres_table_views, meta, 
    Column('id', Integer, primary_key = True), 
    mapped_column(Integer, ForeignKey("users.id"))
    mapped_column(Integer, ForeignKey("papers.id"))
)

meta.create_all(engine)