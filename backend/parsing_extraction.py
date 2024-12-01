import fitz  # PyMuPDF
import re


def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""
    
    # Iterate through each page and extract text
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    return text


def find_references_section(text):
    # Find the start of the references section
    references_start = text.lower().find("references")
    if references_start == -1:
        references_start = text.lower().find("bibliography")
    
    if references_start == -1:
        raise ValueError("References section not found")
    
    # Extract the references section
    references_text = text[references_start:]
    return references_text





def extract_paper_names(references_text):
    # Regular expression to match the start of a reference
    reference_pattern = re.compile(r'^\s*\[\d+\]\s+(.*)', re.MULTILINE)
    
    # Find all matches
    matches = reference_pattern.findall(references_text)
    
    # Remove duplicates by converting to a set, then back to a list
    unique_paper_names = list(set(matches))
    
    return unique_paper_names

