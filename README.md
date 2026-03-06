# TalentScout Hiring Assistant

An AI-powered chatbot that performs an initial technical screening of candidates by collecting their information and generating interview questions based on their declared technology stack.

Live App: https://talentscout-hiring-assistant-dowbugrzvrunjayvltc3do.streamlit.app/
Repository: https://github.com/farajt/talentscout-hiring-assistant

---

## Project Overview

This project implements an AI-based hiring assistant designed to simulate the first stage of a technical recruitment process.

The chatbot interacts with candidates through a web interface and collects essential details such as experience, preferred role, and technical skills. Based on the technologies provided by the candidate, the system generates relevant technical interview questions.

The goal of this project is to demonstrate how Large Language Models (LLMs) can assist recruiters by automating early screening tasks such as gathering candidate information and preparing technical interview questions.

---

## Key Features

The chatbot performs the following steps during the interaction:

**Candidate Greeting**
- Introduces the TalentScout assistant
- Explains the purpose of the screening process

**Information Collection**
The chatbot collects the following details step-by-step:
- Full Name
- Email Address
- Phone Number
- Years of Experience
- Desired Position
- Current Location
- Tech Stack

**Input Validation**
Basic validation is applied to ensure:
- Correct email format
- Valid phone number
- Numeric experience values

**Technical Question Generation**
After the candidate provides their tech stack, the system generates **3–5 interview questions for each technology** listed.

Example:

Tech Stack Input:
```
Python, Django, SQL
```

The chatbot generates interview questions related to Python programming, Django framework concepts, and SQL database knowledge.

**Conversation Flow Management**
The system maintains conversation state and guides the user step-by-step until the screening is completed.

**Data Storage**
Candidate information is stored locally in a JSON file (`candidate_data.json`) for demonstration purposes.

---

## System Architecture

The application follows a simple modular architecture:

```
User Interaction (Streamlit UI)

→ Conversation Handler
→ Candidate Data Validation
→ Tech Stack Processing
→ LLM Question Generation
→ Candidate Summary
→ JSON Data Storage
```

Each module has a specific responsibility, making the project easier to maintain and extend.

---

## Tech Stack

**Backend**
- Python
- LangChain
- Groq API (LLM inference)

**Frontend**
- Streamlit

**Data Storage**
- JSON file for candidate data

**Development Tools**
- Git
- GitHub

---

## Project Structure

```
talentscout-hiring-assistant

app.py
requirements.txt
candidate_data.json

chatbot/
  conversation_handler.py
  question_generator.py
  prompts.py
  llm.py
  memory.py

utils/
  data_store.py
```

**app.py**  
Handles the Streamlit interface and manages user interaction.

**conversation_handler.py**  
Controls the conversation flow and candidate information collection.

**question_generator.py**  
Generates technical interview questions based on the tech stack.

**prompts.py**  
Defines prompts used to guide the language model.

**llm.py**  
Handles communication with the LLM API.

**data_store.py**  
Stores candidate information in a JSON file.

---

## How the System Works

1. The user opens the Streamlit application.
2. The chatbot greets the candidate and explains the screening process.
3. The chatbot collects candidate details step-by-step.
4. The candidate provides their technology stack.
5. The system generates technical interview questions using the LLM.
6. The chatbot displays the candidate summary and generated questions.
7. Candidate information is saved to `candidate_data.json`.

---

## Installation

Clone the repository

```
git clone https://github.com/farajt/talentscout-hiring-assistant
```

Navigate to the project folder

```
cd talentscout-hiring-assistant
```

Create a virtual environment

```
python -m venv venv
```

Activate the environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key

```
GROQ_API_KEY=your_api_key_here
```

Run the application

```
streamlit run app.py
```

The chatbot interface will open in your browser.

---

## Prompt Design

Prompt engineering is used to instruct the language model to generate technical interview questions based on the candidate’s tech stack.

The prompts guide the model to:
- Focus on interview-style technical questions
- Generate multiple questions per technology
- Avoid generic explanations
- Keep the output structured and relevant

This ensures the generated questions are useful for technical screening.

---

## Challenges Faced

One challenge during development was designing a conversation flow that collects candidate information step-by-step while maintaining context throughout the interaction.

Another challenge was ensuring the LLM generates relevant technical interview questions for different technologies. This required prompt tuning to keep the output focused on interview scenarios.

Handling user input validation and unexpected responses was also necessary to ensure a smooth interaction.

---

## Author

Faraj Tamboli  
M.Tech CSE (AI)  
Interested in applied AI systems, LLM applications, and machine learning engineering.