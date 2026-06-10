from data.urls import URLS
from loaders.pdf_loader import load_pdf_documents
from loaders.web_loader import load_web_documents

from processing.metadata import (
    normalize_metadata
)

from processing.chunking import (
    chunk_documents
)

from vectorstore.faiss_manager import (create_vector_store, save_vector_store, load_vector_store, load_or_create_vector_store)

from rag.generator import (generate_answer)

from rag.retrieval import (retrieve_documents)
from rag.context_builder import (build_context)

pdf_docs = load_pdf_documents(
    "data/pdfs"
)

web_docs = load_web_documents(
    URLS
)

all_docs = pdf_docs + web_docs

normalized_docs = normalize_metadata(all_docs)

chunks = chunk_documents(
    normalized_docs
)

vector_store = load_or_create_vector_store(chunks, "fasiss_index")

query = "Who is Frodo?"

results = retrieve_documents(vector_store, query)

context = build_context(results)

answer = generate_answer(
   query,
   context
)

print("\nAnswer:\n")

print(answer)







