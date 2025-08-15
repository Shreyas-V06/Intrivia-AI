def get_router_prompt(user_response, current):
    prompt = f"""
You are an AI Interviewer. 

Decide if the user's reply is to be EVALUATED or NOT , by considering 
the question asked and the user's response to it.

Based on the user's answer and the question asked by the interviewer classify whether the 
    response should be evaluated or not evaluated.
                                                       
    We must evaluate only the responses which are a direct answer to the question asked by the interviewer 
    i.e (Answering the questions: regardless of it being right or wrong, or saying that he cannot answer)
                                                       
    We must not evaluate if the user's response is a clarification question, asking the interviewer to repeat his question or
    anything which does not address the interviewer's question directly
                                                       
    Respond with 
    EVALUATE: if to be evaluated
    DONT_EVALUATE:if not to be evaluated

Question: {current.question}
User Reply: {user_response}
"""
    return prompt
