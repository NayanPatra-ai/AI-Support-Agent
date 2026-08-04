from transformers import pipeline

from config import LLM_MODEL


# Load the model only once
generator = pipeline(
    "text-generation",
    model=LLM_MODEL
)


def generate_answer(question: str, documents):

    context = "\n\n".join([doc.page_content for doc in documents])

    prompt = f"""
You are an OrbitDesk support assistant.

Answer ONLY using the information below.

If the answer is not available, say:
"I couldn't find this information in the documentation."

Documentation:
{context}

Question:
{question}

Answer:
"""

    response = generator(
        prompt,
    max_new_tokens=200,
    do_sample=False,
    return_full_text=False
)

    return response[0]["generated_text"].strip()