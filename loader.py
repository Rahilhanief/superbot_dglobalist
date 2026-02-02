# from langchain_community.document_loaders import CSVLoader

# def load_documents(file_path):
#     loader = CSVLoader(file_path=file_path, encoding="latin-1")  # or 'cp1252'
#     return loader.load()
# loader.py
from langchain_core.documents import Document
import csv

def load_documents(csv_path):
    raw_docs = []
    with open(csv_path, encoding="latin-1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_docs.append(row)
    
    # Convert dicts into Document objects
    docs = []
    for d in raw_docs:
        content = " | ".join([f"{k}: {v}" for k, v in d.items()])  # merge all fields into one string
        docs.append(Document(page_content=content, metadata=d))
    return docs
