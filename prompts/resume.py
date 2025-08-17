from typing import List

def get_summary_prompt(resumeText):
    return f"""As an expert resume analyst, create a comprehensive yet concise summary of this professional profile.

RESUME:
{resumeText}

Please provide a clear, well-structured summary that includes:

1. Professional Overview:
   - Years of experience
   - Core expertise areas
   - Industry focus

2. Key Qualifications:
   - Educational background
   - Major certifications
   - Technical skills

3. Career Highlights:
   - Notable achievements
   - Leadership experience
   - Project impacts

4. Unique Value Proposition:
   - What sets this candidate apart
   - Specialist skills or experiences
   - Notable patterns in career progression

Keep the summary focused on the most relevant and impactful elements of the profile.
Highlight aspects that would be most valuable to potential employers."""



def create_resume_interview_prompt(skills: List[str], experience: str, projects: str, education: str) -> str:
    skills_text = ", ".join(skills)

    return f"""
You are an AI interviewer tasked with generating a **custom interview question set** for a candidate.  
The set must be perfectly tailored to their skills, projects, experience, and education.

Candidate Profile:
-------------------
SKILLS:
{skills_text}

EXPERIENCE:
{experience}

PROJECTS:
{projects}

EDUCATION:
{education}

Your role:
- Generate at least **10 interview questions**.
- Questions must comprehensively cover: 
  1. **Skills** (both conceptual and applied).
  2. **Experience** (scenario/behavioral + real-world applications).
  3. **Projects** (design choices, architecture, challenges, trade-offs).
  4. **Education** (academic foundations, coursework, or theory).
- Vary the types of questions: fundamentals, problem-solving, reasoning/justification, and reflection.

Output Format:
--------------
Question: <The interview question>  
In an ideal answer: <Key points that an excellent answer should cover>  

Guidelines for the "In an ideal answer..." section:
- Provide an evaluation scheme of what makes an excellent response.
- Cover important concepts, keywords, examples, trade-offs, and reasoning paths.
- Length of evaluation scheme: 50-60 words per question**.

Example:
--------
Question: Explain the concept of database indexing and its impact on query performance. 

In an ideal answer: The candidate should define indexing as a data structure that speeds up data retrieval 
while adding storage and write overhead. They should explain common implementations (B-trees, hash indexes), 
types of indexes (primary, secondary, composite, unique), and trade-offs (slower writes, fragmentation, 
increased storage).   

Make sure the questions and evaluation schemes **feel tailored to the candidate's unique profile**.
"""
