from fastapi import APIRouter, File, UploadFile
from prompts.resume import create_resume_interview_prompt
from PyPDF2 import PdfReader
import tempfile
import os
from datetime import datetime
from utils import push_interview_details,convert_qalist_to_dict
from schemas.QAmodel import QASet
from initializers.initialize_llm import initialize_generator_llm
from resume.resume_utils import get_summary
from schemas.QAmodel import ResumeQARequest

resume_router = APIRouter()



@resume_router.post("/create/interview/from-resume")
async def create_interview_from_resume(title:str,desc:str,creator:str,file: UploadFile = File(...)):
    """
    Create an interview QA set from a resume file.
    
    Args:
        file (UploadFile): PDF resume file
        
    Returns:
        dict: Status of interview creation with success flag and message
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        resume_text = ""
        try:
            reader = PdfReader(tmp_path)
            for page in reader.pages:
                resume_text += page.extract_text() or ""
        finally:
            os.remove(tmp_path)

        summary = get_summary(resume_text)
        prompt = create_resume_interview_prompt(skills=summary.skills,experience=summary.experience,projects=summary.projects,education=summary.education)
        llm = initialize_generator_llm()
        llm_so = llm.with_structured_output(QASet)
        qa_object = llm_so.invoke(prompt)
        QAset=convert_qalist_to_dict(qa_object)

        details = {
            'title': title,
            'description': desc,
            'upvotes': 0,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'creator': creator,
            'QAset': QAset[0:15],
            'source': 'resume',
            'tags': summary.skills  
        }

        interview_id = push_interview_details(details)
        
        return {
            'success': True,
            'message': 'Interview created successfully from resume',
            'interview_id': interview_id
        }
            
    except Exception as e:
        return {
            'success': False,
            'message': f'Error creating interview from resume: {str(e)}'
        }
