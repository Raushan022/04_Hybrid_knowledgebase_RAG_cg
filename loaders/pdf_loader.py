from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

def load_pdf_documents(
   pdf_folder_path: str
) -> list[Document]:
   
   pdf_folder = Path(pdf_folder_path)

   pdf_files = list(
      pdf_folder.glob("*.pdf")
   )

   if not pdf_files:
      raise ValueError(
         f"No PDF files found in {pdf_folder_path}"
      )
   
   all_documents = []

   for pdf_file in pdf_files:

      print(f"Loading PDF: {pdf_file.name}")

      loader = PyPDFLoader(
         str(pdf_file)
      )

      documents = loader.load()

      all_documents.extend(documents)

   return all_documents

