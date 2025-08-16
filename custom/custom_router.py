from schemas.QAmodel import CustomQARequest,QASet,PredefinedCustomQARequest
from utils import *
from initializers.initialize_llm import initialize_generator_llm
from datetime import datetime
now=datetime.now()
from fastapi import  APIRouter

custom_router=APIRouter()

@custom_router.post('/create/custom')
def generate_custom_questions(resource:CustomQARequest):
    """
    Generate interview Q&A set from a custom prompt using LLM.

    Args:
        resource (CustomQARequest): Contains prompt, title, description, creator, and tags

    Returns:
        dict: Status with success flag, message, and created interview ID
    """
    llm=initialize_generator_llm()
    llm_so=llm.with_structured_output(QASet)
    object=llm_so.invoke(resource.prompt)
    QAset=convert_qalist_to_dict(object)
    details={
            'title':resource.title,
            'description':resource.description,
            'upvotes':0,
            'date':now.strftime("%Y-%m-%d"),
            'creator':resource.creator,
            'QAset':QAset[0:15],
            'source':'custom',
            'tags':resource.tags
        }
    interview_id=push_interview_details(details)
    status={
            'success':True,
            'message':'Interview has been created',
            'interview_id':interview_id
        }
    return status
    
@custom_router.post('/create/custom/predefined')
def generate_custom_questions(resource:PredefinedCustomQARequest):
    """
    Create interview from predefined Q&A set.

    Args:
        resource (PredefinedCustomQARequest): Contains QAset, title, description, creator, and tags

    Returns:
        dict: Status with success flag, message, and created interview ID
    """
    QAset=resource.QAset
    details={
            'title':resource.title,
            'description':resource.description,
            'upvotes':0,
            'date':now.strftime("%Y-%m-%d"),
            'creator':resource.creator,
            'QAset':QAset[0:15],
            'source':'custom',
            'tags':resource.tags
        }
    interview_id=push_interview_details(details)
    status={
            'success':True,
            'message':'Interview has been created',
            'interview_id':interview_id
        }
    return status
    
