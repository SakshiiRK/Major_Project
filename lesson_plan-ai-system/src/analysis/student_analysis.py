import re

def analyze_student_performance(text):
    """
    Extracts average score from student report text.

    Example:
        "Average score: 62"

    Returns:
        dict
    """
    match = re.search(r"\b(\d{2})\b", text)

    if not match:
        return {"level": "Unknown", "avg": None}

    score = int(match.group(1))

    if score >= 75:
        level = "High"
    elif score >= 50:
        level = "Moderate"
    else:
        level = "Low"

    return {
        "level": level,
        "avg": score
    }