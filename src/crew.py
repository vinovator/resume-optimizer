# src/crew.py
# The orchastrator

from crewai import Crew, Process
from src.config import get_manager_llm
from src.agents import get_agents
from src.tasks import create_analysis_task

def run_resume_crew(resume_text: str, job_text: str, callback_function=None):
    # 1. Get Agents
    tech, culture, writer = get_agents()
    
    # 2. Get Task
    task = create_analysis_task(resume_text, job_text)
    
    # 3. Form Crew
    crew = Crew(
        agents=[tech, culture, writer], # The Committee
        tasks=[task],
        process=Process.hierarchical,   # Manager delegates to them
        manager_llm=get_manager_llm(),  # Gemini runs the show
        verbose=True,
        step_callback=callback_function # to give spinner updates in U
    )
    
    return crew.kickoff()
