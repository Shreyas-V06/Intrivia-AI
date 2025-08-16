def get_router_prompt(user_response, current):
    prompt = f"""
You are an AI Interviewer. 

Decide if the user's reply is to be EVALUATED or NOT , by considering 
the question asked and the user's response to it.

Based on the user's answer and the question asked by the interviewer classify whether the 
    response should be evaluated or not evaluated.
                                                       
    We must evaluate only the responses which are a direct answer to the question asked by the interviewer 
    i.e (Answering the questions: regardless of it being right or wrong, or saying that he cannot answer)
     
     Examples for which you must EVALUATE
     - Answer to the question
     - Saying that he does not know the answer (will be given zero score)
     - Saying abusive languages (will be given zero score)
     - Manipulation tactics(will be given zero)
     - Any requests to skip the question (will be given zero)
     - reattempt the previous question(will be given zero)

    We must not evaluate if the user's response is a clarification question, asking the interviewer to repeat his question or
    anything which does not address the interviewer's question directly.

     Example for which you must NOT EVALUATE:
     - repeat the current question
     - doubts for clarification
    
     
                                                       
    Respond with 
    EVALUATE: if to be evaluated
    DONT_EVALUATE:if not to be evaluated

Question: {current.question}
User Reply: {user_response}
"""
    return prompt
