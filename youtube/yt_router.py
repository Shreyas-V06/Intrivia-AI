from fastapi import  APIRouter
from youtube.yt_utils import *
from schemas.QAmodel import *
from datetime import datetime
from utils import *
now=datetime.now()

yt_router = APIRouter()

@yt_router.post('/create/youtube')
async def get_qa_from_yt(resource:YouTubeQARequest):
    try:
        transcript=transcribe_yt_to_str(resource.url)
        object=qa_from_yt(transcript)
        QAset=convert_qalist_to_dict(object)
        details={
            'title':resource.title,
            'description':resource.description,
            'upvotes':0,
            'date':now.strftime("%Y-%m-%d"),
            'creator':resource.creator,
            'QAset':QAset[0:15],
            'source':'youtube',
            'tags':resource.tags
        }
        interview_id=push_interview_details(details)
        status={
            'success':True,
            'message':'Interview has been created',
            'interview_id':interview_id
        }
        return status
    except Exception as e:
        status={
            'success':False,
            'message':'Please ensure the provided YouTube video is accessible and contains English subtitles or audio for transcription.'
        }
        return status
