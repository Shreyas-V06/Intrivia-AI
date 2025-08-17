from pydantic import BaseModel, Field
from typing import List

class ResumeSummary(BaseModel):
    skills: List[str] = Field(
        description="""
        A list of all technical skills mentioned in the resume. This includes:
        - Programming languages (e.g., Python, JavaScript)
        - Frameworks and libraries (e.g., React, FastAPI, Langchain)
        - Tools and platforms (e.g., Git, Docker, Postman)
        - Databases (e.g., MongoDB, PostgreSQL)

        Each item should be a single technical skill as a string. Extract only those explicitly mentioned in the resume.
        """
    )

    experience: str = Field(
        description="""
        A summarized string containing the candidate's work or internship experience.
        Include role titles, company names, technologies used, and a brief description of responsibilities or outcomes.
        This should be a concise yet informative summary of all relevant experience from the resume.
        """
    )

    projects: str = Field(
        description="""
        A summarized string describing all projects mentioned in the resume.
        For each project, include the name, its purpose or outcome, and the tech stack used.
        The summary should focus on relevant technical or academic projects that demonstrate the applicant's skills.
        """
    )

    education: str = Field(
        description="""
        A summarized string of the candidate's educational background.
        Include the degree(s), institution name(s), and optionally the years attended or performance (GPA/percentage).
        The summary should clearly present the academic qualifications in one paragraph.
        """
    )