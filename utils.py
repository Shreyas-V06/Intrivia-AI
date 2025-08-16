
import os
from typing import List
from schemas.QAmodel import QASet,QAItem
from initializers.initialize_llm import initialize_llm
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from initializers.initialize_db import initialize_db
from prompts.search import get_custom_interview_prompt
import uuid
load_dotenv()
def convert_qalist_to_dict(qa_set: QASet) -> List[dict]:
    result = []
    
    for qa_item in qa_set.QAList:
        qa_dict = {
            'question': qa_item.question,
            'answer': qa_item.answer
        }
        result.append(qa_dict)
    
    return result

def convert_dict_to_qaitem(data: dict) -> QAItem:
    return QAItem(
        question=data.get('question'),
        answer=data.get('answer')
    )


tavily_api_key=os.getenv('TAVILY_API_KEY')
tavily_tool=TavilySearch()

@tool
def search_internet_tool(query:str):
    """Searches the internet with a query"""
    result=tavily_tool.invoke(query)
    return result
tools=[search_internet_tool]

def get_start_question():
    question=f"""Good morning. I am Intrivia AI, and I'll be conducting your interview today.
    Lets begin. Could you please introduce youself?"""
    answer="""An ideal answer should begin with the candidate's name and current role or area of study, followed by a brief overview of their background, skills, or 
    experiences relevant to the opportunity they signed up for."""
    return {'question':question,'answer':answer}

def get_end_question():
    question="END OF INTERVIEW"
    answer="END OF INTERVIEW"
    return {'question':question,'answer':answer}

def internet_agent(query:str):
    prompt=get_custom_interview_prompt()
    llm=initialize_llm()
    llm_tool=create_react_agent(llm,tools=tools,prompt=prompt)
    result=llm_tool.invoke({"messages": [{"role": "user", "content": query}]})
    return result

def push_interview_details(details):
    db=initialize_db()
    collection=db.Intrivia
    start=get_start_question()
    interview_id=str(uuid.uuid4())
    details['interview_id']=interview_id
    details['QAset'].insert(0,start)
    end=get_end_question()
    details['QAset'].append(end)


    collection.interviews.insert_one(details).inserted_id
    return interview_id