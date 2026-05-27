import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from tools import extract_youtube_transcript

load_dotenv()

gemini_engine=LLM(
    model=os.getenv("MODELNAME", "gemini/gemini-2.5-flash"),
    api_key=os.getenv("GEMINI_API_KEY")
)

extraction_task= Task(
    description="Extraction"
)