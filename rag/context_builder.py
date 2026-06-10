from langchain_core.documents import Document

def build_context(
      documents: list[Document]
) -> str:
   
   if not documents:
      raise ValueError("No documents provided")
   
   context_parts = []

   for doc in documents:
      source_name = doc.metadata.get(
         "source_name",
         "unknown source"
      )

      context_parts.append(
         f"Source: {source_name}\n\n"
         f"{doc.page_content}"
      )

      context = "\n\n" + (
         "\n\n" + "-" * 50 + "\n\n"
      ).join(context_parts)

      return context