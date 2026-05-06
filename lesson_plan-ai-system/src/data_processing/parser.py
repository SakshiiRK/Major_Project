import re

def split_lessons(file_path):
    """
    Splits raw lesson file into individual lessons.

    Args:
        file_path (str): Path to lesson file

    Returns:
        list: List of lesson texts
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    lessons = re.split(r"LESSON PLAN NO\s*\.\d+", text)
    return [l.strip() for l in lessons if len(l.strip()) > 100]


def extract_sections(lesson):
    """
    Extracts structured sections from a lesson.

    Args:
        lesson (str): Full lesson text

    Returns:
        dict: Extracted sections
    """
    def extract(keyword):
        pattern = rf"{keyword}:(.*?)(?=\n[A-Z ]+:|\Z)"
        match = re.search(pattern, lesson, re.DOTALL)
        return match.group(1).strip() if match else ""

    return {
        "objectives": " ".join([line for line in extract("OBJECTIVES").split("\n") if len(line) > 5]),
        "method": extract("TEACHING METHOD"),
        "activity": extract("ACTIVITY"),
        "presentation": extract("PRESENTATION"),
        "full_text": lesson
    }