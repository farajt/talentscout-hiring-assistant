import os
import streamlit as st
from langchain_groq import ChatGroq


def get_llm():

    # Load API key
    api_key = None

    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
    else:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found")

    llm = ChatGroq(
        groq_api_key=api_key,
        model="llama3-8b-8192",
        temperature=0.2,
        max_tokens=800
    )

    return llm