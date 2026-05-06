import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("API key not found")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ UPDATED
        messages=[
            {"role": "system", "content": "You are an expert in educational pedagogy."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content