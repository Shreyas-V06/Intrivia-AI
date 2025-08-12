from schemas.QAmodel import *
from initializers.initialize_llm import initialize_llm
from initializers.initialize_db import initialize_db
from prompts.youtube import get_yt_prompt
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract


def qa_from_yt(transcript:str)->QASet:
    llm=initialize_llm()
    prompt=get_yt_prompt(transcript)
    llm_so = llm.with_structured_output(QASet)
    object= llm_so.invoke(prompt)
    return object


def transcribe_yt_to_str(url:str)->str:
    result=""
    video_id=extract.video_id(url)
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript=ytt_api.fetch(video_id)
    for snippet in fetched_transcript:
        result+=snippet.text
    return result


