from utils.data_store import save_candidate_data
import re
from chatbot.question_generator import generate_questions


# -------------------------------
# Step Indicator
# -------------------------------

def get_step_indicator(step):

    steps = {
        1: "Step 1/7 — Collecting Candidate Name",
        2: "Step 2/7 — Collecting Email Address",
        3: "Step 3/7 — Collecting Phone Number",
        4: "Step 4/7 — Collecting Experience",
        5: "Step 5/7 — Collecting Desired Position",
        6: "Step 6/7 — Collecting Location",
        7: "Step 7/7 — Collecting Tech Stack",
    }

    return steps.get(step, "")


# -------------------------------
# Validation Functions
# -------------------------------

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_experience(exp):
    return exp.isdigit()


# -------------------------------
# Conversation Handler
# -------------------------------

def handle_user_input(user_input, session_state):

    user_input = user_input.strip()

    if "step" not in session_state:
        session_state.step = 0

    if "candidate" not in session_state:
        session_state.candidate = {
            "name": "",
            "email": "",
            "phone": "",
            "experience": "",
            "position": "",
            "location": "",
            "tech_stack": []
        }

    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        return (
            "Thank you for completing the **TalentScout technical screening**.\n\n"
            "Our recruitment team will review your responses and contact you regarding the next steps.\n\n"
            "We appreciate your time!"
        )


# -------------------------------
# Step 0 → Greeting
# -------------------------------

    if session_state.step == 0:

        session_state.step = 1

        return (
            "Hello! Welcome to **TalentScout Hiring Assistant**.\n\n"
            "I will collect a few details and generate technical interview questions based on your tech stack.\n\n"
            "Your information will only be used for recruitment screening.\n\n"
            f"{get_step_indicator(1)}\n\n"
            "**What is your full name?**"
        )


# -------------------------------
# Step 1 → Name
# -------------------------------

    elif session_state.step == 1:

        session_state.candidate["name"] = user_input
        session_state.step = 2

        return (
            f"{get_step_indicator(2)}\n\n"
            "Please enter your **email address**."
        )


# -------------------------------
# Step 2 → Email
# -------------------------------

    elif session_state.step == 2:

        if not validate_email(user_input):
            return "That doesn't look like a valid **email address**. Please enter a valid email."

        session_state.candidate["email"] = user_input
        session_state.step = 3

        return (
            f"{get_step_indicator(3)}\n\n"
            "Please enter your **phone number (10 digits)**."
        )


# -------------------------------
# Step 3 → Phone
# -------------------------------

    elif session_state.step == 3:

        if not validate_phone(user_input):
            return "Please enter a valid **10-digit phone number**."

        session_state.candidate["phone"] = user_input
        session_state.step = 4

        return (
            f"{get_step_indicator(4)}\n\n"
            "How many **years of experience** do you have?"
        )


# -------------------------------
# Step 4 → Experience
# -------------------------------

    elif session_state.step == 4:

        if not validate_experience(user_input):
            return "Please enter a **valid number** for years of experience."

        session_state.candidate["experience"] = user_input
        session_state.step = 5

        return (
            f"{get_step_indicator(5)}\n\n"
            "What **position** are you applying for?"
        )


# -------------------------------
# Step 5 → Position
# -------------------------------

    elif session_state.step == 5:

        session_state.candidate["position"] = user_input
        session_state.step = 6

        return (
            f"{get_step_indicator(6)}\n\n"
            "What is your **current location**?"
        )


# -------------------------------
# Step 6 → Location
# -------------------------------

    elif session_state.step == 6:

        session_state.candidate["location"] = user_input
        session_state.step = 7

        return (
            f"{get_step_indicator(7)}\n\n"
            "Please list your **tech stack** separated by commas.\n\n"
            "Example:\n"
            "Python, Django, SQL, Docker"
        )


# -------------------------------
# Step 7 → Tech Stack
# -------------------------------

    elif session_state.step == 7:

        tech_stack = [tech.strip() for tech in user_input.split(",")]

        session_state.candidate["tech_stack"] = tech_stack

        # Save candidate data
        save_candidate_data(session_state.candidate)

        questions = generate_questions(tech_stack)

        summary = f"""
### Candidate Summary

**Name:** {session_state.candidate['name']}  
**Email:** {session_state.candidate['email']}  
**Phone:** {session_state.candidate['phone']}  
**Experience:** {session_state.candidate['experience']} years  
**Position:** {session_state.candidate['position']}  
**Location:** {session_state.candidate['location']}  
**Tech Stack:** {", ".join(tech_stack)}

---

### Technical Questions
"""

        session_state.step = 8

        return summary + questions


# -------------------------------
# Step 8 → End
# -------------------------------

    else:

        return (
            "Thank you for completing the screening.\n\n"
            "Our recruitment team will contact you soon.\n\n"
            "Type **exit** to end the conversation."
        )