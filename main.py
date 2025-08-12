from youtube.yt_router import yt_router
from agent.agent_router import agent_router
from general.query_router import query_router
from custom.custom_router import custom_router
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
app.include_router(agent_router)
app.include_router(query_router)
app.include_router(custom_router)