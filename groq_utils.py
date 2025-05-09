import os
import fitz
from groq import Groq
import json

# Load API Key
def load_api_key():
    """
    Loads the GROQ_API_KEY from config.json or environment variables.
    """
    try:
        with open("config.json") as f:
            return json.load(f)["GROQ_API_KEY"]
    except Exception as e:
        print(f"Error loading API Key: {e}")
        return os.getenv("GROQ_API_KEY", "")

# Initialise Groq Client
def init_groq_client():
    """
    Initialises the Groq client with the API key.
    """
    api_key = load_api_key()
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please set it in `config.json` or as an environment variable.")
    return Groq(api_key=api_key)

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from the uploaded PDF file.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

# Generate Flashcards using Groq
def get_flashcard_prompt(text_chunk):
    """
    Generates the prompt for the flashcard generation request.
    """
    return f"""
You are an expert learning assistant. Read the study material below and create helpful flashcards.

Return Q&A pairs in this format:
Q: What is X?
A: X is Y.

Use clear, concise language. No introduction text. Just flashcards.

STUDY MATERIAL:
\"\"\"{text_chunk}\"\"\"
"""

def generate_flashcards(client, text_chunk):
    """
    Generates flashcards using Groq's language model.
    """
    prompt = get_flashcard_prompt(text_chunk)
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }],
            temperature=0.3,
            max_completion_tokens=1024,
            top_p=1.0,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating flashcards: {str(e)}"
