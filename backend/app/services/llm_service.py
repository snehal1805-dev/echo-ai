import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv("GEMINI_MODEL")


def ask_llm(question: str, context: list[str]) -> str:
    """
    Sends the retrieved context + user question to Gemini.
    """

    context_text = "\n\n".join(context)

    prompt = f"""
You are Echo AI.

Answer ONLY using the document context below.

If the answer is not present, reply exactly:

"I couldn't find that information in the uploaded documents."

Document Context:

{context_text}

Question:

{question}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text