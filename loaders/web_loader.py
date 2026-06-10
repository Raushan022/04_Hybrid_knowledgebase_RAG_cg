from langchain_core.documents import Document
from langchain_community.document_loaders import WebBaseLoader

def load_web_documents(
      urls: list[str]
) -> list[Document]:
   if not urls:
      raise ValueError(
         "No URLs Found"
      )
   
   all_documents = []

   for url in urls:
      try:
         print(f"Loading URL: {url}")

         loader = WebBaseLoader(url)
         documents = loader.load()

         all_documents.extend(documents)

      except Exception as error:
         print(f"Failed loading {url}")

         print(error)

   return all_documents