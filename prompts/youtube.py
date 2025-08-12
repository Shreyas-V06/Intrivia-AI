
def get_yt_prompt(transcript:str):
    prompt=f"""You are an expert interview analyst and question curator.
    Your task is to process the following YouTube transcript and extract an exhaustive list of interview-style questions
    with evaluation scheme pairs.

    Instructions:
    #IMPORTANT: Avoid any form of formating through the use of #(hashtags),-(hyphens),*(astricks)
    all the generated content should be in form of words only

    1. Identify all possible questions — include both:
    Explicitly asked questions in the transcript.
    Implied or natural interview questions based on the flow of conversation.

    2. For each question:
    - Make it clear, unambiguous, and context-independent.
    - Remove names, company references, or any transcript-specific details.
    - Ensure it sounds professional and natural, as if directly asked in a real interview.

    3. For each evaluation scheme:
    - Do not write the answer directly, rather just give a brief outline about what all points should be
        covered in an ideal answer.
    - Include all domain-specific knowledge, facts, and concepts relevant to answering the question.
        however just naming them is enough. 
    - Summarize key points and keywords.
    - Remove filler words, irrelevant tangents, and non-verbal cues.

    Example:
    For the question-> What are the Benefits of ReactJS?
    An expected output for evaluation scheme would be:

    An ideal answer should highlight that ReactJS offers a component-based architecture, enabling developers to create reusable 
    and modular UI components that improve maintainability and scalability.
    It should mention the Virtual DOM, which optimizes rendering performance by updating only the parts of the UI that change. 
    Knowledge of JSX as a syntax extension that enhances code readability and developer productivity is expected. 
    The answer should also reference React's large community, extensive ecosystem, and strong support for third-party libraries.
    Awareness of server-side rendering for SEO benefits, cross-platform capabilities via React Native, and availability of developer tools
    for debugging and profiling is also appreciated. A complete answer should convey how these features combine to improve development efficiency, 
    application performance, and long-term maintainability.


    4. Preserve the logical order of questions as they appear or could appear in the interview.

    Now perform the task for the following Transcript:
    {transcript}

    """
    return prompt