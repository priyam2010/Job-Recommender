import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env vars from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("Missing GOOGLE_API_KEY in .env")

# Create Gemini chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key,  # Explicit API key
    temperature=0.5
)

# Test prompt
response = llm.invoke("List 3 internship roles for someone with Python and SQL skills.")
print(response.content)