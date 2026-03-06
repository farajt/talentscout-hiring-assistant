import os
import streamlit as st
from langchain_groq import ChatGroq

def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        api_key = st.secrets.get("GROQ_API_KEY")

    return ChatGroq(
        model="llama3-70b-8192",
        groq_api_key=api_key,
        temperature=0.3
    )