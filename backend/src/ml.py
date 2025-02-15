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
 
ps = PorterStemmer()

class PapersHandler:

    def __init__(self):

        with open('/home/admin/PSP/backend/pdfs/filtered_paper2idpaperid.pickle', 'rb') as handle:
            self.filtered_paper2idpaperid = pickle.load(handle)
        with open('/home/admin/PSP/backend/pdfs/paperid2filtered_paperid.pickle', 'rb') as handle:
            self.paperid2filtered_paperid = pickle.load(handle)
        with open('/home/admin/PSP/backend/pdfs/papers.pickle', 'rb') as handle:
            self.papers = pickle.load(handle)

        f = 30
        self.annoy_index = AnnoyIndex(f, 'euclidean')
        self.annoy_index.load('/home/admin/PSP/backend/pdfs/papers.ann') # super fast, will just mmap the file
    
    def get_similar_articles(self, paper_id, top_n=5):

        filtered_paperid = self.paperid2filtered_paperid[int(paper_id)]
        filtered_paperids = self.annoy_index.get_nns_by_item(filtered_paperid, 1 + top_n)[1:]
        paperids = [
            self.filtered_paper2idpaperid[filtered_paperid] 
            for filtered_paperid in filtered_paperids]
        
        return [
            {
                'id': paperid,
                'title': self.papers[paperid]['title'],
                'link': self.generate_citation_link(self.papers[paperid])
            }
            for paperid in paperids
        ]
        
    def search(self, query: str):
        query_stems = set(ps.stem(w) for w in query.split())

        results = []
        for paperid, filtered_paperid in self.paperid2filtered_paperid.items():
            paper = self.papers[paperid]
            if len(paper['stems'] & query_stems)> 0:
                results.append({
                    'id': paperid,
                    'title': paper['title']
                })

        return results


    def ger_paper(self, id: str):
        paper = self.papers[int(id)]
        return {
            'title': paper['title'],
            'pdf_url': self.generate_pdf_url(id),
            'link': self.generate_citation_link(paper)}
    
    
    def generate_citation_link(self, paper):
        return f"{paper['author']} et al. {paper['year']}. {paper['title']}"


    def generate_pdf_url(self, id):
        return f'http://localhost:5000/article/{id}'
        

    def get_pdf_path(self, id: str):
        return f"../pdfs/{id}.pdf"
        


