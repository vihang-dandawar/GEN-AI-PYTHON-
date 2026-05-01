from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings
# Load environment variables
load_dotenv()

# PDF path
pdfpath = Path(__file__).parent / "CORE_JAVA_INTERVIEW_QUESTIONS.pdf"

# Load PDF
loader = PyPDFLoader(file_path=pdfpath)
docs = loader.load()   # Splits PDF page-wise

print(docs[12])  # Print page 13

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(docs)

#  Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store vectors in Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_RAG"
)

print("Indexing part is done...")