import pandas as pd
from src.data_processing.parser import split_lessons, extract_sections
from src.data_processing.labeling import label_bloom, label_teaching_style


def build_dataset(input_path, output_path):
    lessons = split_lessons(input_path)

    data = []

    for lesson in lessons:
        sections = extract_sections(lesson)

        combined_text = (
            sections["objectives"] +
            sections["method"] +
            sections["presentation"]
        )

        bloom = label_bloom(combined_text)
        style = label_teaching_style(combined_text)

        data.append({
            "text": combined_text,
            "bloom": bloom,
            "style": style
        })

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)

    print("Dataset created:", df.shape)