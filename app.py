import streamlit as st
from parser import extract_text
from ats_score import calculate_score
from keyword_match import keyword_analysis
from skills import detect_skills
from suggestions import generate_suggestions
from report import create_report
from analysis import explain_match
from sections import check_sections

st.title("AI Resume ATS Checker")

resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_description = st.text_area("Paste Job Description")

if resume_file and job_description:

    resume_text = extract_text(resume_file)

    score = calculate_score(resume_text, job_description)

    explanation = explain_match(score)

    matched, missing = keyword_analysis(resume_text, job_description)

    sections_found = check_sections(resume_text)

    skills = detect_skills(resume_text)

    suggestions = generate_suggestions(score, missing, sections_found)

    report = create_report(score, skills, matched, missing, suggestions)

    st.subheader("ATS Score")
    st.write(score)

    st.subheader("Match Explanation")
    st.write(explanation)

    st.subheader("Skills Found")
    st.write(skills)

    st.subheader("Matched Keywords")
    st.write(matched)

    st.subheader("Missing Keywords")
    st.write(missing)

    st.subheader("Resume Sections Detected")
    st.write(sections_found)

    st.subheader("Suggestions")
    for s in suggestions:
        st.write("-", s)

    st.download_button(
        "Download Resume Report",
        report.to_csv(index=False),
        file_name="resume_analysis.csv",
        mime="text/csv"
    )