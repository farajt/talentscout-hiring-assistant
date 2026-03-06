import streamlit as st
from chatbot.conversation_handler import handle_user_input, get_step_indicator

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Custom CSS Styling
# -------------------------

st.markdown("""
<style>

.main-title {
    font-size:36px;
    font-weight:700;
    text-align:center;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.chat-box {
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

.user-box {
    background-color:#e6f3ff;
}

.bot-box {
    background-color:#f5f5f5;
}

.summary-card {
    background-color:#f0f7ff;
    padding:20px;
    border-radius:12px;
    border:1px solid #d0e3ff;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("📌 About This Project")

    st.write("""
**TalentScout Hiring Assistant**

An AI-powered chatbot designed to automate the **initial technical screening process** for candidates.

### Features
- Collects candidate information
- Validates user inputs
- Generates technical interview questions
- Maintains conversation context
- Stores candidate data

### Technologies
- Python
- Streamlit
- LangChain
- Groq LLM
""")

    st.write("---")

    st.write("👨‍💻 Developed for AI/ML Internship Assignment")

# -------------------------
# Title Section
# -------------------------

st.markdown('<div class="main-title">🤖 TalentScout Hiring Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI assistant that collects candidate details and generates technical interview questions.</div>', unsafe_allow_html=True)

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = 0

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

# -------------------------
# Progress Indicator
# -------------------------

progress = min(st.session_state.step / 7, 1.0)

st.progress(progress)

if st.session_state.step > 0 and st.session_state.step <= 7:
    st.info(get_step_indicator(st.session_state.step))

# -------------------------
# Display Chat Messages
# -------------------------

for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f'<div class="chat-box user-box"><b>You:</b><br>{message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="chat-box bot-box"><b>Assistant:</b><br>{message["content"]}</div>',
            unsafe_allow_html=True
        )

# -------------------------
# Chat Input
# -------------------------

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    response = handle_user_input(user_input, st.session_state)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()

# -------------------------
# Candidate Summary Card
# -------------------------

if st.session_state.step == 8 and st.session_state.candidate:

    candidate = st.session_state.candidate

    st.markdown("""
    <div class="summary-card">
    <h3>Candidate Information</h3>
    """, unsafe_allow_html=True)

    st.write(f"**Name:** {candidate.get('name','')}")
    st.write(f"**Email:** {candidate.get('email','')}")
    st.write(f"**Phone:** {candidate.get('phone','')}")
    st.write(f"**Experience:** {candidate.get('experience','')} years")
    st.write(f"**Position:** {candidate.get('position','')}")
    st.write(f"**Location:** {candidate.get('location','')}")
    st.write(f"**Tech Stack:** {', '.join(candidate.get('tech_stack', []))}")

    st.markdown("</div>", unsafe_allow_html=True)