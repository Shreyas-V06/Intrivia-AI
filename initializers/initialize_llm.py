import os
from dotenv import load_dotenv
import google.generativeai as genai 
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

def initialize_llm():
    GeminiApiKey=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GeminiApiKey)
    GeminiLLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    return GeminiLLM

