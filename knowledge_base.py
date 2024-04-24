
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

# Loading documents
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import JSONLoader

# Chroma db
from langchain.vectorstores.chroma import Chroma

# Embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

# Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter


DB_PATH = "./chroma"
PDFS_PATH = "./data/pdf"
def load_documents():
    loader = PyPDFDirectoryLoader(PDFS_PATH,extract_images=True)
    documents = loader.load()
    return documents


def create_embeddings(documents):
     # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
        add_start_index=True,
    )
    
    chunks = text_splitter.split_documents(documents)
    
    # Create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-ada-002")
    return chunks, embeddings 

def save_to_db(chunks, embeddings):
     # Clear the chroma directory if it exists
    if (os.path.exists(DB_PATH)):
        shutil.rmtree(DB_PATH)

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to chroma DB at {DB_PATH}")
    

if __name__ == "__main__":
    documents = load_documents()
    #print(f"Loaded {len(documents)} documents from the PDF directory")
    chunks, embeddings  = create_embeddings(documents)
    
    #Test the chunks
    document = chunks[2]
    print(document.page_content)
    print(document.metadata)
    
    save_to_db(chunks, embeddings)
