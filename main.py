from youtube.yt_router import yt_router
from interviewer.interviewer_router import interviewer_router
from interviewer.evaluation_router import evaluation_router
from general.query_router import query_router
from general.update_router import update_router
from custom.custom_router import custom_router
from resume.resume_router import resume_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
    expose_headers=["Content-Type"], 
)
app.include_router(yt_router)
app.include_router(interviewer_router)
app.include_router(query_router)
app.include_router(custom_router)
app.include_router(update_router)
app.include_router(resume_router)
app.include_router(evaluation_router)