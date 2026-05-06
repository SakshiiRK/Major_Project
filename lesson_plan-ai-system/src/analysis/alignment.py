def check_alignment(objectives, co, po):
    text = objectives.lower()

    score = 0
    if co and co.lower() in text:
        score += 1
    if po and po.lower() in text:
        score += 1

    if score == 2:
        return {"status": "Well Aligned", "reason": "Matches CO & PO"}
    elif score == 1:
        return {"status": "Partial", "reason": "Matches one"}
    return {"status": "Misaligned", "reason": "No alignment"}