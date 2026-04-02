import streamlit as st
from src.inference.pipeline import run_pipeline

st.title("Lesson Plan Analyzer")

text = st.text_area("Paste Lesson Plan")

if st.button("Analyze"):
    result = run_pipeline(text)

    st.subheader("Results")
    st.write("Bloom Level:", result["Bloom Level"])
    st.write("Teaching Style:", result["Teaching Style"])
    st.write("Performance Insight:", result["Performance Insight"])

    st.subheader("Feedback")
    for f in result["Feedback"]:
        st.write("-", f)