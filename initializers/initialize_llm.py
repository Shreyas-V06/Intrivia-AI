import os
from dotenv import load_dotenv
import google.generativeai as genai 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

def initialize_generator_llm():
    GeminiApiKey=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GeminiApiKey)
    GeminiLLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    return GeminiLLM

def initialize_llm():
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    return llm