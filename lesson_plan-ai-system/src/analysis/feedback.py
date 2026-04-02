def generate_feedback(bloom, style):
    feedback = []

    if bloom in ["Remember", "Understand"]:
        feedback.append("Increase higher-order thinking tasks (Analyze/Evaluate).")

    if style == "Lecture-based":
        feedback.append("Add interactive or activity-based learning.")

    if style == "Activity-based":
        feedback.append("Good engagement. Ensure concept clarity.")

    if bloom in ["Analyze", "Evaluate", "Create"]:
        feedback.append("Strong cognitive level maintained.")

    return feedback