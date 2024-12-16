from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from llm_chains import load_vectordb, create_embeddings
import pypdfium2
import chromadb
import yaml


with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


#extracts text from document
def get_pdf_texts(pdf_files):
    return [extract_text_from_pdf(pdf_bytes) for pdf_bytes in pdf_files]

#loads text from pdf and joins
def extract_text_from_pdf(pdf_bytes):
    pdf_file =  pypdfium2.PdfDocument(pdf_bytes)
    return "\n".join(pdf_file.get_page(page_number).get_textpage().get_text_range() for page_number in range(len(pdf_file)))
    
# converts the text to chunks
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap = 50, separators = ["\n","\n\n"])
    return splitter.split_text(text)


def get_document_chunks(text_list):
    documents = []
    for text in text_list:
        for chunk in get_text_chunks(text):
            # print(chunk)
            documents.append(Document(page_content=chunk))
    return documents

# add chunks to vectordb
def add_documents_to_db(pdf_bytes):
    texts = get_pdf_texts(pdf_bytes)
    documents = get_document_chunks(texts)

    vector_db = load_vectordb(create_embeddings())
    vector_db.delete_collection()
    vector_db = load_vectordb(create_embeddings())
    vector_db.add_documents(documents)
    print("Document added to db")
