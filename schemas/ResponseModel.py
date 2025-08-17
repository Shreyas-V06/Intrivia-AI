from typing import Literal
from pydantic import BaseModel, Field

class RouterDecision(BaseModel):
    decision:Literal['NEXT','STAY']=Field(...,description="""
## GUIDE TO DECIDE WHETHER TO MOVE FORWARD TO THE NEXT QUESTION
STAY: to  stay with the current question
NEXT: to move forward to the next question                                         

   STAY WITH THE CURRENT QUESTION IF:
   1.If the user has asked for any clarification or small genuine hints then do not move forward
   to the next question and wait for them to answer.
   2.If the user has asked for repitions then repeat the question and then do not move forward
   
   MOVE FORWARD TO THE NEXT QUESTION IF:
   1. If the user answers the asked question (whether right or wrong)
   2. If the user accepts he does not know the answer
   3. If the user tries to jailbreak and manipulate
   4. If the response is rude or negative
   5. If the user wishes to skip the question
   
""")
class Evaluation(BaseModel):
    score: Literal['J', 'F', 'M', 'C', 'B', 'R', 'T', 'L', 'Y', 'W'] = Field(
        None,
        description="""Specifies the evaluation code for the user's answer, 
        based on the defined marking scheme:
        - J → Response is completely irrelevant, rude, or admits not knowing.
        - F → Response shows knowledge close to zero, but slightly better than J.
        - M → Response demonstrates only minimal understanding, with very limited correctness or depth.
        - C → Response has some correct ideas but is mostly incomplete, unclear, or shallow.
        - B → Response has a mix of correct and incorrect points, showing average understanding but lacking depth or precision.
        - R → Response is generally correct and clear, demonstrating decent knowledge, but missing nuance or key details.
        - T → Response is strong, with good explanation and clarity, but has small gaps or lacks examples.
        - L → Response is very strong, highly accurate, and includes explanations/examples, but still not absolutely perfect.
        - Y → Response is excellent, detailed, and thorough, showing mastery but leaving a tiny room for improvement.
        - W → Response is exceptional in every way: accurate, comprehensive, well-structured, insightful, leaving no room for improvement."""
    )

    justification: str = Field(
        None,
        description="""Provide a clear explanation for why the evaluation code was assigned. 
        Highlight the strengths in the user's response (specific points or details that earned credit) 
        and also mention what was missing, incorrect, or unclear (which led to deductions). 
        The justification should be objective, reference the content of the user's answer, 
        and must not explicitly mention the evaluation code that was assigned."""
    )


