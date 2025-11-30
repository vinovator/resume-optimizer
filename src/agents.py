# src/agents.py
# Define the workers

from crewai import Agent
from src.config import get_worker_llm


def get_agents():
    llm = get_worker_llm()
    

    # Agent 1: The Hard Skill Validator
    tech_screener = Agent(
        role="HR & Tech Screener",
        goal="Verify hard requirements: Skills, Location, Education, and Years of Experience.",
        backstory="""You are a strict ATS algorithm. 
        You check four things: 
        1. Do they have the Tech Skills? 
        2. Do they have the Degree? 
        3. Do they have the Years of Experience? 
        4. Are they in the right Location?
        You are binary and logical.""",
        llm=llm,
        verbose=True
    )

    # Agent 2: The Soft Skill/Culture Profiler
    culture_analyst = Agent(
        role="Culture Fit Analyst",
        goal="Assess soft skills and leadership traits.",
        backstory="You are an HR Manager. You look for soft skills mentioned in the job description. You judge the tone of the resume.",
        llm=llm,
        verbose=True
    )

    # Agent 3: The Resume Writer (The Fixer)
    writer = Agent(
        role="Professional Resume Writer",
        goal="Rewrite sections to maximize the match score.",
        backstory="You are a top-tier career coach. You know how to rephrase a boring bullet point into a high-impact achievement using the missing keywords.",
        llm=llm,
        verbose=True
    )
    
    return tech_screener, culture_analyst, writer
