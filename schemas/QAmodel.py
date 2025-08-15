from pydantic import Field,BaseModel
from typing import List,Optional,Dict

class QAItem(BaseModel):
    question:str = Field(..., description="""This field will contain a question extracted from the Youtube transcript.
    The question should be:
    1. Clearly framed and unambiguous.
    2. Professionally worded so it can be directly asked in any interview setting.
    3. Independent of transcript-specific references (e.g., remove names, prior discussion mentions, or company-specific context).
    4. Natural-sounding, grammatically correct, and well-punctuated.
""")
    answer:str=Field(...,description="""This field will contain an exhaustive list of points and keywords to be contained in the 
    answer to the aforementioned question.
    1.The answer should contain all the domain-specific relevant knowledge which is expected in the answer.
    2.The answer should be properly framed and unambigious""")

class QASet(BaseModel):
    QAList:List[QAItem] = Field(..., description="""This field contains an exhaustive list of question-answer pairs extracted from the YouTube transcript.
    Each item in the list should follow the QAItem schema, where:                         
    1. The 'question' field is a clearly framed, professional, and context-independent interview question.
    2. The 'answer' field contains an exhaustive, well-structured set of points and keywords representing the expected domain-specific response.                    
    The list should preserve the logical sequence in which questions appear in the transcript.""")

class YouTubeQARequest(BaseModel):
    url: str
    title: str
    description: str
    creator: str
    tags: List[str]

class CustomQARequest(BaseModel):
    prompt:str
    title: str
    description: str
    creator: str
    tags: List[str]

class PredefinedCustomQARequest(BaseModel):
    QAset:List[Dict]
    title: str
    description: str
    creator: str
    tags: List[str]
    