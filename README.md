# Job-Recommender
## Project Description
This project is an AI-powered web application that recommends jobs and internships to students based on their skills, preferences, and experience.
It uses LangChain and Google Gemini API with a Retrieval-Augmented Generation (RAG) approach to personalize recommendations. The UI is built using Streamlit, and the backend integrates skill-matching with AI-powered contextual analysis for better job matching accuracy.

## Features
1. Skill Based search - Matches jobs based on user skills, experience, and preferences.

2. AI-Powered Recommendations – Uses Gemini LLM to enhance relevance and personalization.

3. RAG Integration – Retrieves job descriptions from a database for accurate AI responses.

4. Streamlit UI – Clean, interactive, and easy to use.

## How to Run
### Install Dependencies
Make sure Python 3.10+ is installed.

Install dependencies.

### Set Environment Variables 
Sign up for Google AI Studio and get your Gemini API key.

Store it in an environment variable.
###  Prepare Your Files
Save your backend logic (LangChain + Gemini RAG) in one Python file (e.g., rag_pipeline.py).

Create your Streamlit UI file (e.g., app.py) to interact with the backend.
### Run the App

In your project folder, run:

streamlit run app.py

   


