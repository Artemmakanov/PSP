import sys

sys.path.append('/home/ubuntu/Documents/PSP/src')

from parsing_extraction import get_referenced_titles
from pprint import pprint
import arxiv
from tqdm import tqdm
from pathlib import Path
import logging
import pickle

class Paper:
    def __init__(self, id, url, title, author, published, refs):
        self.id = id
        self.url = url
        self.title = title
        self.author = author
        self.published = published
        self.refs = refs
    
    def __repr__(self):
        return f"{self.id}_{self.url}_{self.title}_{self.author}"+\
            f"{self.published}_{self.refs}"


if __name__ == "__main__":
    # Construct the default API client.
    dirpath = "/home/admin/PSP/backend/pdfs"
    max_results = 10_000

    client = arxiv.Client()
    request = 'recommender'
    search = arxiv.Search(
        query = request,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.Relevance
    )

    papers = []
    id = 0
    for paper_arxiv in tqdm(client.results(search), desc='Processing papers', total=max_results):
        # Download the PDF to a specified directory with a custom filename.
        try:
            paper_arxiv.download_pdf(dirpath=dirpath, filename=f"{id}.pdf",)
            
            pdf_path = Path(dirpath) / f"{id}.pdf"

            paper_names = get_referenced_titles(str(pdf_path))

            papers.append(Paper(id, paper_arxiv.entry_id,  paper_arxiv.title, paper_arxiv.authors, paper_arxiv.published, paper_names))


            with open(Path(dirpath) / f'papers_stucture_{request}.pickle', 'wb') as handle:
                pickle.dump(papers, handle, protocol=pickle.HIGHEST_PROTOCOL)

            id += 1
            
        except Exception as e:
            print(e)
            logging.info(f"Paper {paper_arxiv.title} can not be downloaded!")
            continue

        
        