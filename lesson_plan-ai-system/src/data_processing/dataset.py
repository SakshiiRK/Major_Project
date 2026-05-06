import pandas as pd
from src.data_processing.parser import split_lessons, extract_sections
from src.data_processing.labeling import label_bloom, label_teaching_style


def build_dataset(input_path, output_path):
    """
    Builds dataset CSV from raw lesson file.

    Args:
        input_path (str)
        output_path (str)

    Returns:
        None
    """
    lessons = split_lessons(input_path)

    data = []

    for lesson in lessons:
        sections = extract_sections(lesson)

        text = sections["objectives"] + sections["method"]

        data.append({
            "text": text,
            "bloom": label_bloom(text),
            "style": label_teaching_style(text)
        })

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)

    print("Dataset created:", df.shape)