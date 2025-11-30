# src/models.py
# Structured JSON Output

from pydantic import BaseModel, Field
from typing import List

class ResumeAnalysis(BaseModel):
    match_score: int = Field(..., description="Overall score 0-100 based on all criteria.")

    # --- HARD REQUIREMENTS (The Checkboxes) ---
    # Tech
    missing_hard_skills: List[str] = Field(..., description="List of technical keywords missing from the resume.")
    hard_skills_score: int = Field(..., description="Score 0-100 for technical skills.")

    # Experience (Years, Seniority)
    missing_experience: List[str] = Field(..., description="Specific experience gaps (e.g., 'Missing 2 years of management exp').")
    experience_score: int = Field(..., description="Score 0-100 for seniority/experience fit.")

    # Education
    education_gap: str = Field(..., description="Any gap in education (e.g., 'Requires Masters, has Bachelors') or 'None'.")
    education_score: int = Field(..., description="Score 0-100 for education requirements.")

    # Location
    location_status: str = Field(..., description="The candidate's location status (e.g., 'In-State', 'Relocation Needed', 'Remote').")
    location_score: int = Field(..., description="Score 0-100. 0 if visa/location mismatch, 100 if perfect.")

    # --- SOFT REQUIREMENTS (The Vibe) ---
    missing_soft_skills: List[str] = Field(..., description="List of soft skills missing (e.g. Leadership, Communication).")
    soft_skills_score: int = Field(..., description="Score 0-100 for cultural/tone alignment.")

    # --- THE OUTPUTS ---
    tailored_summary: str = Field(..., description="A rewritten Professional Summary aligned with the job description.")
    improved_bullets: List[str] = Field(..., description="3 examples of rewritten resume bullet points that include the missing keywords.")