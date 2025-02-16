import pickle

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.ml import PapersHandler, generate_citation_link, get_pdf_path, generate_pdf_url
from src.db_models import Papers, Base

from nltk.stem import PorterStemmer

 
ps = PorterStemmer()

ph = PapersHandler()

engine = create_engine('postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/recsys')

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

with open('/home/admin/PSP/backend/data/papers.pickle', 'rb') as handle:
    papers = pickle.load(handle)

# Вставка данных
for paperid, paper in enumerate(papers):

    p = Papers(
        id=paperid, 
        title=paper["title"], 
        stems=",".join(list(set(ps.stem(w) for w in paper["title"].split()))),
        link_ru=generate_citation_link(papers[paperid]),
        link_en='',
        filepath=get_pdf_path(paperid)
    )
    session.add(p)

session.commit()
session.close()