from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from pathlib import Path

load_dotenv()

def create_vector_store(
      chunks: list[Document]
) -> FAISS:
   
   if not chunks:
      raise ValueError("No chunks provided")
   
   embeddings = OpenAIEmbeddings(
      model="text-embedding-3-small"
   )

   print(
    f"Creating vector store from "
    f"{len(chunks)} chunks..."
   )

   vector_store = FAISS.from_documents(
      chunks,
      embeddings
   )

   return vector_store


def save_vector_store(
      vector_store: FAISS,
      save_path: str
) -> None:
   
   vector_store.save_local(save_path)

   print(f"vector store saved to {save_path}")


def load_vector_store(
      save_path: str
) -> FAISS:
   
   embeddings = OpenAIEmbeddings(
      model="text-embedding-3-small"
   )

   vector_store = FAISS.load_local(
      save_path,
      embeddings,
      allow_dangerous_deserialization=True
   )

   print(f"Vector store loaded from {save_path}")

   return vector_store

def load_or_create_vector_store(
      chunks: list[Document],
      save_path: str
) -> FAISS:
   
   if Path(save_path).exists():
      print("Existing vector store found.")

      return load_vector_store(save_path)
   
   print("No vector store found")

   vector_store = create_vector_store(chunks)

   save_vector_store(
      vector_store,
      save_path
   )

   return vector_store