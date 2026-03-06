import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Works locally (.env) and on Streamlit Cloud (secrets)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        raise ValueError("GROQ_API_KEY not found. Please set it in .env or Streamlit secrets.")