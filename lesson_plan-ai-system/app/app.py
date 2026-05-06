import streamlit as st
from src.inference.pipeline import run_pipeline
from src.utils.pdf_reader import extract_text_from_pdf

st.title("AI Lesson Plan Analyzer")

lesson_file = st.file_uploader("Upload Lesson Plan PDF", type=["pdf"])
student_file = st.file_uploader("Upload Student Report (Optional)", type=["pdf"])

if st.button("Analyze"):

    if lesson_file:
        lesson_text = extract_text_from_pdf(lesson_file)

        student_text = ""
        if student_file:
            student_text = extract_text_from_pdf(student_file)

        result = run_pipeline(lesson_text, student_text)

        st.subheader("Model Output")
        st.write("Bloom Level:", result["bloom"])
        st.write("Teaching Style:", result["style"])
        st.write("Learning Impact:", result["impact"])

        st.write("CO:", result["co"])
        st.write("PO:", result["po"])

        st.subheader("Student")
        st.write("Level:", result["student"]["level"])

        st.subheader("Detailed Report")
        st.write(result["report"])

    else:
        st.warning("Upload lesson plan PDF")