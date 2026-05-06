def learning_impact(bloom, student_level):
    if student_level == "Low" and bloom in ["Remember", "Understand"]:
        return "Low Impact"
    if student_level == "High" and bloom in ["Analyze", "Evaluate", "Create"]:
        return "High Impact"
    return "Moderate Impact"