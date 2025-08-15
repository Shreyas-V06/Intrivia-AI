from typing import Literal
from pydantic import BaseModel, Field

class RouterDecision(BaseModel):
    decision:Literal['EVALUATE','DONT_EVALUATE']=Field(...,description="""Based on the user's answer and the question asked by the interviewer classify whether the 
    response should be evaluated or not evaluated.
                                                       
    We must evaluate only the responses which are a direct answer to the question asked by the interviewer 
    i.e (Answering the questions: regardless of it being right or wrong, or saying that he cannot answer)
                                                       
    We must not evaluate if the user's response is a clarification question, asking the interviewer to repeat his question or
    anything which does not address the interviewer's question directly
                                                       
    Respond with 
    EVALUATE: if to be evaluated
    DONT_EVALUATE:if not to be evaluated
   
    """)

class Evaluation(BaseModel):
    score: Literal['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] = Field(
        None,
        description="""Specifies the score for the user's answer out of 10. Where 0 is the least 
        possible score and 10 is the highest possible score.
        The score must be given sensibly but still leniently. consider all the relevant sections of answer and 
        comparing it with the expected evaluation. If the answer somewhat matches with the expected answer
        give them decent marks, if its perfect then give them 10, and if its unrelated then give low marks (below 2)"""
    )

    justification: str = Field(
        None,
        description="""Justification of the score that has been given for the user's answer, 
        It must mention the reason for which the mark has been awarded and the reason for deductions. 
        Properly reference the sections by mentioning the points which earned them marks or 
        lack of points which resulted in them losing marks."""
    )


class Response(BaseModel):
    response:str=Field(...,description="""
    The appropriate response to be given to the candidate. 
      
    """)