import os
import streamlit as st
from langchain_groq import ChatGroq


def get_llm():

    # Get API key from Streamlit secrets or environment
    api_key = None

    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please add it in Streamlit Secrets.")

    llm = ChatGroq(
        groq_api_key=api_key,
        model="mixtral-8x7b-32768",
        temperature=0.3
    )

    return llm