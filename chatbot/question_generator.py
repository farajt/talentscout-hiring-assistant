from chatbot.llm import get_llm
from langchain_core.messages import HumanMessage


def generate_questions(tech_stack):

    llm = get_llm()

    questions_output = ""

    for tech in tech_stack:

        prompt = f"""
You are a technical interviewer.

Generate exactly 5 technical interview questions for the following technology.

Technology: {tech}

Rules:
- Do NOT include introductions
- Do NOT explain anything
- Only return the questions
- Format as a numbered list

Example format:

1. Question
2. Question
3. Question
4. Question
5. Question
"""

        try:
            response = llm.invoke(
                [HumanMessage(content=prompt)]
            )

            questions_output += f"\n\n### {tech}\n\n"
            questions_output += response.content.strip()

        except Exception:
            questions_output += f"\n\n### {tech}\n\n"
            questions_output += "Unable to generate questions for this technology at the moment."

    return questions_output