from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from config.settings import TOP_K

def retrieve_documents(
      vector_store: FAISS,
      query: str,
      k: int=TOP_K
) -> list[Document]:
   
   if not query.strip():
      raise ValueError("Query can not be empty")
   
   documents = (
      vector_store.similarity_search(
         query=query,
         k=k
      )
   )

   return documents

