import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")

# Initialize embeddings and Chroma db
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def retrieve(query: str) -> str:
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])
