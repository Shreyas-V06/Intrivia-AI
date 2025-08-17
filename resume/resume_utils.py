from initializers.initialize_llm import initialize_generator_llm
from prompts.resume import get_summary_prompt
from schemas.ResumeSummary import ResumeSummary

def get_summary(resumeText):
    llm=initialize_generator_llm()
    llm_so = llm.with_structured_output(ResumeSummary)
    prompt = get_summary_prompt(resumeText)
    summary= llm_so.invoke(prompt)
    return summary


