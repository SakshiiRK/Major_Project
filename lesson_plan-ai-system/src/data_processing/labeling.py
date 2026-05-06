def label_bloom(text):
    """
    Strong rule-based Bloom classification with weights.
    """
    if not text:
        return "Understand"

    text = text.lower()

    levels = {
        "Remember": ["define", "list", "identify", "recall"],
        "Understand": ["explain", "describe", "summarize"],
        "Apply": ["apply", "solve", "use"],
        "Analyze": ["analyze", "compare", "differentiate"],
        "Evaluate": ["evaluate", "justify", "assess"],
        "Create": ["create", "design", "develop"]
    }

    weights = {
        "Remember": 1,
        "Understand": 2,
        "Apply": 3,
        "Analyze": 4,
        "Evaluate": 5,
        "Create": 6
    }

    scores = {}

    for level, words in levels.items():
        count = sum(text.count(w) for w in words)
        scores[level] = count * weights[level]

    best = max(scores, key=scores.get)

    return best if scores[best] > 0 else "Understand"


def label_teaching_style(text):
    """
    Assigns teaching style.

    Args:
        text (str)

    Returns:
        str
    """
    text = text.lower()

    if "activity" in text:
        return "Activity-based"
    elif "discussion" in text or "question" in text:
        return "Inquiry-based"
    elif "project" in text:
        return "Project-based"

    return "Lecture-based"