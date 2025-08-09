import streamlit as st
from src.llm_engine import get_recommendations

st.title("Job Recommender")

# User input
skills = st.text_input("Enter your skills (comma-separated)")
experience = st.text_area("Describe your experience")
preferences = st.text_input("Any preferences? (location, type of work, etc.)")

# Resume upload
uploaded_resume = st.file_uploader("Upload your resume (optional)", type=["txt", "pdf"])

resume_text = None
if uploaded_resume is not None:
    if uploaded_resume.type == "text/plain":
        resume_text = uploaded_resume.read().decode("utf-8")
    else:
        st.warning("PDF parsing not implemented yet — please upload a .txt file")

# Mode selection
mode = st.radio("Choose Recommendation Mode", ["direct", "rag"])

# Get recommendations
if st.button("Get Recommendations"):
    if not skills and not resume_text:
        st.error("Please enter skills or upload a resume.")
    else:
        recommendations = get_recommendations(skills, experience, preferences, resume_text, mode)
        st.subheader("Recommended Jobs:")
        st.write(recommendations)