from pathlib import Path
from langchain_core.documents import Document

def normalize_metadata(
      documents: list[Document]
) -> list[Document]:
   
   for doc in documents:
      source = doc.metadata.get("source", "")

      if source.startswith('http'):
         doc.metadata["source_type"] = "web"

         title = doc.metadata.get("title", "Unknwon Website")

         doc.metadata["source_name"] = (
            title.split(" - ")[0]
         )

      else:
         doc.metadata["source_type"] = "pdf"

         doc.metadata["source_name"] = (
            Path(source).name
         )

   return documents