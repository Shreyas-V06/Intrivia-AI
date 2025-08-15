from typing import TypedDict,Annotated,Sequence
from langchain_core.messages import BaseMessage
from interviewer.interviewer_utils import reducer

class SharedState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],reducer]
    user_response:Annotated[str,reducer]
    interview_id:Annotated[str,reducer]
    question_id:Annotated[int, reducer]
    router_decision:Annotated[bool, reducer]
  

