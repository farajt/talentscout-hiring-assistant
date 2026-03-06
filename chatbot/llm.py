import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


def get_llm():
    """
    Initialize and return the Groq LLM using LangChain.
    """

    load_dotenv()

    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    return llm