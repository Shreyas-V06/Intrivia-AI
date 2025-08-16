from typing import TypedDict,Annotated,Sequence
from langchain_core.messages import BaseMessage
from interviewer.interviewer_utils import reducer
from langgraph.graph import add_messages

class SharedState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],reducer,add_messages]
    user_response:Annotated[str,reducer]
    interview_id:Annotated[str,reducer]
    question_id:Annotated[int, reducer]
    router_decision:Annotated[bool, reducer]
  

