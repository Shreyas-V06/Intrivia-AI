from schemas.SharedState import SharedState
from schemas.ResponseModel import *
from langchain_core.messages import AIMessage
from initializers.initialize_llm import *
from interviewer.interviewer_utils import get_current_question_item
from prompts.responder import get_responder_prompt
from prompts.evaluator import get_evaluator_prompt
from prompts.router import get_router_prompt

llm=initialize_llm()

def responder(state:SharedState):
    user_response=state['user_response']
    current = get_current_question_item(state['interview_id'],state['question_id'])
    next = get_current_question_item(state['interview_id'],state['question_id']+1)
    prompt=get_responder_prompt(response=user_response,question=current.question,queue=next.question)
    response=llm.invoke(prompt)
    state['messages'].append(response)
    return state

def router(state:SharedState):
    user_response = state["user_response"]
    current = get_current_question_item(state['interview_id'],state['question_id'])
    llm_so=llm.with_structured_output(RouterDecision)
    prompt=get_router_prompt(user_response,current)
    object=llm_so.invoke(prompt)
    state['router']=True
    if(object.decision=='EVALUATE'):
        state['router_decision']=True
    else:
        state['router_decision']=False
    return state

def evaluator(state:SharedState):
    user_response = state["user_response"]
    current_question = get_current_question_item(state['interview_id'],state['question_id'])
    llm_so=llm.with_structured_output(Evaluation)
    prompt=get_evaluator_prompt(user_response,current_question.question,current_question.answer)
    object=llm_so.invoke(prompt)
    return state

def join_node(state:SharedState):
    #Fan-in node
    return state

