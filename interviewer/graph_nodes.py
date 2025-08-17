from schemas.SharedState import SharedState
from schemas.ResponseModel import *
from initializers.initialize_llm import *
from interviewer.interviewer_utils import get_current_question_item
from prompts.responder import get_responder_prompt
from prompts.evaluator import get_evaluator_prompt
from prompts.router import get_router_prompt
from langchain_core.messages import HumanMessage

llm=initialize_llm()

def responder(state:SharedState):
    user_response=state['user_response'][-1].content
    current = get_current_question_item(state['interview_id'],state['question_id'])
    message="Current question: "+current.question+"\nUser Response: "+user_response
    state['messages'].append(HumanMessage(content=message))
    prompt=get_responder_prompt()
    system_prompt={"role":"system","content":prompt}
    response=llm.invoke([system_prompt]+state['messages'])
    state['messages'].append(response)
    return state

def router(state:SharedState):
    user_response=state['user_response'][-1].content
    current=get_current_question_item(state['interview_id'],state['question_id'])
    llm_so=llm.with_structured_output(RouterDecision)
    prompt=get_router_prompt(user_response=user_response,question=current.question)
    object=llm_so.invoke(prompt)
    state['router']=True
    if(object.decision=='NEXT'):
        state['router_decision']=True
    else:
        state['router_decision']=False
    return state

def evaluator(state:SharedState):
    user_response=state['user_response'][-1].content
    current_question = get_current_question_item(state['interview_id'],state['question_id'])
    llm_so=llm.with_structured_output(Evaluation)
    prompt=get_evaluator_prompt(user_response,current_question.question,current_question.answer)
    object=llm_so.invoke(prompt)
    state['score']=object.score
    state['suggestion']=object.justification
    return state

def join_node(state:SharedState):
    return state

