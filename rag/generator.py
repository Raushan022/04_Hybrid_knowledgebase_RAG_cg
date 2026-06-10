from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME

load_dotenv()

def generate_answer(
      query: str,
      context: str
) -> str: 
   
   llm = ChatOpenAI(
      model=MODEL_NAME
   )

   prompt = f"""
You are a helpful LOTR assistant.

Use only the provided context
to answer the question.

If the answer cannot be found
in the context, say:

"I could not find that information
in the provided sources."

context:
{context}

Question:
{query}

Answer:
"""
   response = llm.invoke(prompt)

   return response.content