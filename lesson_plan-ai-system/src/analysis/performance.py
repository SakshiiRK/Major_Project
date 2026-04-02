def analyze_performance(bloom, style):
    score = 0

    bloom_score = {
        "Remember": 1,
        "Understand": 2,
        "Apply": 3,
        "Analyze": 4,
        "Evaluate": 5,
        "Create": 6
    }

    style_score = {
        "Lecture-based": 1,
        "Activity-based": 2,
        "Inquiry-based": 3,
        "Project-based": 4
    }

    score += bloom_score.get(bloom, 2)
    score += style_score.get(style, 1)

    if score >= 8:
        return "High Learning Impact"
    elif score >= 5:
        return "Moderate Learning Impact"
    return "Low Learning Impact"