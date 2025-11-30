# src/config.py
# Hybrid LLM setup

import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_manager_llm():
    return LLM(
        model="gemini-2.5-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    )


# def get_worker_llm():
#     return LLM(
#         model="ollama/llama3.1",
#         base_url="http://localhost:11434"
#     )


def get_worker_llm():
    return LLM(
        model="gemini-2.5-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    )