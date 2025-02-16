import pickle
import pandas as pd
from tqdm import tqdm
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import numpy as np
from annoy import AnnoyIndex

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_models import Users, Favourites, Papers
from .config import conf

engine = create_engine(conf.postgres_url)    

ps = PorterStemmer()

class PapersHandler:

    def __init__(self):

        with open('/home/admin/PSP/backend/pdfs/filtered_paper2idpaperid.pickle', 'rb') as handle:
            self.filtered_paper2idpaperid = pickle.load(handle)
        with open('/home/admin/PSP/backend/pdfs/paperid2filtered_paperid.pickle', 'rb') as handle:
            self.paperid2filtered_paperid = pickle.load(handle)

        # with open('/home/admin/PSP/backend/pdfs/papers.pickle', 'rb') as handle:
        #     self.papers = pickle.load(handle)

        f = 30
        self.annoy_index = AnnoyIndex(f, 'euclidean')
        self.annoy_index.load('/home/admin/PSP/backend/pdfs/papers.ann') # super fast, will just mmap the file
    
    def get_similar_articles(self, paper_id, top_n=5):

        filtered_paperid = self.paperid2filtered_paperid[int(paper_id)]
        filtered_paperids = self.annoy_index.get_nns_by_item(filtered_paperid, 1 + top_n)[1:]
        paperids = [
            self.filtered_paper2idpaperid[filtered_paperid] 
            for filtered_paperid in filtered_paperids]
        
        results = []

        for paperid in paperids:
            paper = self.get_paper(paperid)
            results.append(
                {
                    'id': paperid,
                    'title': paper['title'],
                    'link': paper['link']
                } 
            )
        return results
        
    def search(self, query: str):
        query_stems = set(ps.stem(w) for w in query.split())

        results = []
        for paperid, filtered_paperid in self.paperid2filtered_paperid.items():
            paper = self.get_paper(paperid)
            if len(paper['stems'] & query_stems)> 0:
                results.append({
                    'id': paperid,
                    'title': paper['title']
                })

        return results


    def get_paper(self, id: str):
        Session = sessionmaker(engine)
        with Session() as session:
            paper = session.query(Papers).filter_by(id=id).first()

        return {
            'title': paper.title,
            'pdf_url': paper.filepath,
            'link': paper.link_ru,
            'stems': set(paper.stems.split(','))}
    



def generate_citation_link(paper):
    return f"{paper['author']} et al. {paper['year']}. {paper['title']}"


def get_pdf_path(id: str):
    return f"../pdfs/{id}.pdf"


def generate_pdf_url(id):
    return f'http://localhost:5000/article/{id}'
    

        