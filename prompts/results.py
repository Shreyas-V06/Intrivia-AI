def create_summary_prompt(suggestions):
    return f"""You are an AI assistant for an AI interviewer, your job is to 
    study the suggestions given by the interviewer to each of user's response
    and then come up with an Overview for the entire interview.
    
    The overview should be a small paragraph, consisting of only the body section with 
    no headings or formatting.

    Suggestions:
    {suggestions}"""