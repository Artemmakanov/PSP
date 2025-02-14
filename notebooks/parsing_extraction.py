import re
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Извлекает текст из PDF-файла."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text

def extract_references(text):
    """Извлекает названия статей из списка литературы."""
    references = []
    ref_pattern = re.compile(r'\[\d+\]\s+.*?\.\s+(.*?)\.\s+In\s+[A-Z]+', re.DOTALL)  
    matches = ref_pattern.findall(text)
    
    for match in matches:
        references.append(match.strip())
    
    return references

def get_referenced_titles(pdf_path):
    """Основная функция для извлечения заголовков статей, на которые ссылается документ."""
    text = extract_text_from_pdf(pdf_path)
    references = extract_references(text)
    return references
