import sys

sys.path.append('/home/ubuntu/Documents/PSP/src')

from parsing_extraction import extract_text_from_pdf, find_references_section, extract_paper_names
from pprint import pprint
import arxiv
from tqdm import tqdm
from pathlib import Path
import pickle

class Paper:
    def __init__(self, url, title, author, published, refs):
        self.url = url
        self.title = title
        self.author = author
        self.published = published
        self.refs = refs
    
    def __repr__(self):
        return f"{self.url}_{self.title}_{self.author}"+\
            f"{self.published}_{self.refs}"


if __name__ == "__main__":
    # Construct the default API client.
    dirpath = "/home/ubuntu/Documents/PSP/dump"
    max_results = 10_000

    client = arxiv.Client()
    
    # Search for the 10 most recent articles matching the keyword "quantum."
    search = arxiv.Search(
    query = "recsys",
    max_results = max_results,
    sort_by = arxiv.SortCriterion.Relevance
    )

    papers = []
    for paper_arxiv in tqdm(client.results(search), desc='Processing papers', total=max_results):
        # Download the PDF to a specified directory with a custom filename.
        try:
            paper_arxiv.download_pdf(dirpath=dirpath, filename=f"{paper_arxiv.title}.pdf",)
            
        except:
            continue

        
        pdf_path = Path(dirpath) / f"{paper_arxiv.title}.pdf"
        
        text = extract_text_from_pdf(str(pdf_path))

        references_text = find_references_section(text)

        paper_names = extract_paper_names(references_text)

        papers.append(Paper(paper_arxiv.entry_id,  paper_arxiv.title, paper_arxiv.authors, paper_arxiv.published, paper_names))


        with open(Path(dirpath) / 'papers_stucture.pickle', 'wb') as handle:
            pickle.dump(papers, handle, protocol=pickle.HIGHEST_PROTOCOL)