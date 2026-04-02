from .inference import Predictor
from src.analysis.performance import analyze_performance
from src.analysis.feedback import generate_feedback

# Label maps (VERY IMPORTANT)
bloom_labels = [
    "Remember", "Understand", "Apply",
    "Analyze", "Evaluate", "Create"
]

style_labels = [
    "Lecture-based", "Activity-based",
    "Inquiry-based", "Project-based"
]

# Load models once
bloom_model = Predictor("models/bloom_model")
style_model = Predictor("models/style_model")


def run_pipeline(text):
    bloom = bloom_model.predict(text, bloom_labels)
    style = style_model.predict(text, style_labels)

    performance = analyze_performance(bloom, style)
    feedback = generate_feedback(bloom, style)

    return {
        "Bloom Level": bloom,
        "Teaching Style": style,
        "Performance Insight": performance,
        "Feedback": feedback
    }