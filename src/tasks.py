# src/tasks.py
# The comprehensive instructions

from crewai import Task
from src.models import ResumeAnalysis

def create_analysis_task(resume: str, job_desc: str):
    return Task(
        description=f"""
        Analyze this resume against the job description.
        
        JOB DESCRIPTION:
        {job_desc}
        
        RESUME:
        {resume}
        
        your specific instructions:
        
        1. "HR & Tech Screener": Check the HARD Requirements.   <-- MATCHES EXACTLY NOW
           - Tech Skills (Keywords)
           - Education (Degree match?)
           - Experience (Years match?)
           - Location (Is the candidate local?)
           
        2. "Culture Fit Analyst": Check the SOFT Requirements.  <-- MATCHES EXACTLY NOW
        
        3. "Professional Resume Writer": Rewrite the Summary... <-- MATCHES EXACTLY NOW
        
        4. Calculate specific scores for each category (0-100) and a final weighted match score.
        """,
        expected_output="A structured ATS analysis report.",
        output_pydantic=ResumeAnalysis
    )