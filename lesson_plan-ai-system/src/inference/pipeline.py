from src.inference.inference import Predictor
from src.data_processing.parser import extract_sections
from src.analysis.student_analysis import analyze_student_performance
from src.analysis.performance import learning_impact
from src.analysis.co_po_extractor import extract_co_po
from src.llm.report_generator import generate_report

bloom_labels = ["Remember","Understand","Apply","Analyze","Evaluate","Create"]
style_labels = ["Lecture-based","Activity-based","Inquiry-based","Project-based"]

bloom_model = Predictor("models/bloom_model")
style_model = Predictor("models/style_model")


def run_pipeline(lesson_text, student_text=None):
    sections = extract_sections(lesson_text)

    objectives = sections.get("objectives", "")
    method = sections.get("method", "")
    activity = sections.get("activity", "")

    # 🔹 Model predictions
    bloom = bloom_model.predict(objectives, bloom_labels)
    style = style_model.predict(method, style_labels)

    # 🔹 Engagement
    engagement = "High" if "group" in activity.lower() else "Low"

    # 🔹 Student performance
    student = analyze_student_performance(student_text or "")

    # 🔹 CO-PO extraction (NEW)
    co_po = extract_co_po(lesson_text)

    # 🔹 Learning impact
    impact = learning_impact(bloom, student["level"])

    # 🔹 LLM input
    report = generate_report({
        "bloom": bloom,
        "style": style,
        "engagement": engagement,
        "student": student,
        "co": co_po["co"],
        "po": co_po["po"]
    })

    return {
        "bloom": bloom,
        "style": style,
        "impact": impact,
        "student": student,
        "co": co_po["co"],
        "po": co_po["po"],
        "report": report
    }