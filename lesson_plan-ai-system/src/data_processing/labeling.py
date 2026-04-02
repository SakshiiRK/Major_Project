def label_bloom(text):
    text = text.lower()

    if "define" in text:
        return "Remember"
    elif "explain" in text or "understand" in text:
        return "Understand"
    elif "apply" in text:
        return "Apply"
    elif "analyze" in text:
        return "Analyze"
    elif "evaluate" in text:
        return "Evaluate"
    elif "create" in text:
        return "Create"
    return "Understand"


def label_teaching_style(text):
    text = text.lower()

    if "activity" in text:
        return "Activity-based"
    elif "question" in text or "discussion" in text:
        return "Inquiry-based"
    elif "project" in text:
        return "Project-based"
    return "Lecture-based"