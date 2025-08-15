from fastapi import  APIRouter
from langchain_core.messages import HumanMessage
from interviewer.graph_builder import graph
interviewer_router=APIRouter()

@interviewer_router.post('/interview')
def interact_with_interviewer(user_answer:str,question_id:int,session_id:str,interview_id:str):
    config = {"configurable": {
    "thread_id": session_id
    }}
    state={
        "messages":[HumanMessage(content=user_answer)],
        "interview_id":interview_id,
        "question_id":question_id,
        "router_decision":True,
        "user_response":user_answer

    }
    response=graph.invoke(state,config=config)
    if(response['router_decision']):
        response['question_id']+=1
    result=  { 'response':response['messages'][-1].content,
               'question_id':response['question_id'],
             }
    return result
