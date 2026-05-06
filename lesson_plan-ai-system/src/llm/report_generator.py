from src.llm.groq_client import call_llm

def generate_report(data):
    """
    Generates detailed teaching report.
    """

    prompt = f"""
You are an expert in education analysis.

Lesson Analysis:
- Bloom Level: {data['bloom']}
- Teaching Strategy: {data['style']}
- Engagement: {data['engagement']}

Student Performance:
- Average Score: {data['student']['avg']}
- Level: {data['student']['level']}

CO:
{data['co']}

PO:
{data['po']}

Tasks:
1. Evaluate lesson effectiveness
2. Check alignment with CO and PO
3. Identify gaps
4. Suggest improvements

Return structured output.
"""

    return call_llm(prompt)