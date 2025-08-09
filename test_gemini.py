import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Correct model name
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Test it
response = model.generate_content("Python SQL jobs?")
print(response.text)