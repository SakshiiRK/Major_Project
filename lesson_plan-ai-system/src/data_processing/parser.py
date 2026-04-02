import re

def split_lessons(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    lessons = re.split(r"LESSON PLAN NO\s*\.\d+", text)
    lessons = [l.strip() for l in lessons if len(l.strip()) > 100]

    return lessons


def extract_sections(lesson):
    def extract(keyword):
        pattern = rf"{keyword}:(.*?)(?=\n[A-Z ]+:|\Z)"
        match = re.search(pattern, lesson, re.DOTALL)
        return match.group(1).strip() if match else ""

    return {
        "objectives": extract("OBJECTIVES"),
        "method": extract("TEACHING METHOD"),
        "presentation": extract("PRESENTATION"),
        "activity": extract("ACTIVITY"),
        "full_text": lesson
    }