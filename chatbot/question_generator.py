from chatbot.llm import get_llm


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

        response = llm.invoke(prompt)

        questions_output += f"\n\n### {tech}\n\n"
        questions_output += response.content.strip()

    return questions_output