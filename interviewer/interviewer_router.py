from fastapi import  APIRouter
from langchain_core.messages import HumanMessage
from interviewer.graph_builder import graph
from interviewer.interviewer_utils import get_current_question_item
from utils import *
interviewer_router=APIRouter()


@interviewer_router.post('/interview')
def interact_with_interviewer(user_answer:str,question_id:int,session_id:str,interview_id:str):
    """
    Process user's interview answer and return next question or feedback.

    Args:
        user_answer (str): Candidate's response to the current question
        question_id (int): Current question identifier
        session_id (str): Interview session ID (to be generated at client side)
        interview_id (str): Interview template ID

    Returns:
        dict: Response containing feedback/next question, question_id, and exit status
    """

    config = {"configurable": {
    "thread_id": session_id
    }}

    
    state={
        "messages":[HumanMessage(content=user_answer)],
        "interview_id":interview_id,
        "question_id":question_id,
        "router_decision":True,
        "user_response":user_answer,
        "score":"J",
        "suggestion":"None"
    }

    response=graph.invoke(state,config=config)
    next_question_id=response['question_id']
    next_question=""
    if(response['router_decision']):
        next_question_id=response['question_id']+1
        next_question=form_question(get_current_question_item(state['interview_id'],next_question_id).question)
        push_suggestion_details(code_to_score(response['score'][-1].content),response['suggestion'][-1].content,session_id)

    item=get_current_question_item(response['interview_id'],next_question_id)

    if(item.question=='END OF INTERVIEW' and item.answer=='END OF INTERVIEW'):
        result= { 'response':"Alright , Thank you for your time today. That concludes your interview. I will review your responses and get back to you with the results shortly.",
               'question_id':0,
                'is_exit':True
             }
    else:
        result=  { 'response':response['messages'][-1].content + next_question,
               'question_id':next_question_id,
                'is_exit':False
             }
    return result
