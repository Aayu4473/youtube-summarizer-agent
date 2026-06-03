import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from tools import extract_youtube_transcript

load_dotenv()

gemini_engine=LLM(
    model=os.getenv("MODELNAME", "gemini/gemini-2.5-flash"),
    api_key=os.getenv("GEMINI_API_KEY")
)

extractor=Agent(
    role="Senior YouTube Data Extractor",
    goal="Extract the exact transcript from the provided YouTube URL.",
    backstory="You are an expert data pipeline engineer. You use tools to reliably extract raw text from videos.",
    tools=[extract_youtube_transcript],
    llm=gemini_engine,
    allow_delegation=False
)
synthesizer=Agent(
    role="Executive summary synthesizer",
    goal="Transform raw transcripts into highly readable, actionable bullet points.",
    backstory="You are a Chief of Staff who reads long transcripts and gives the CEO exactly what they need to know.",
    llm=gemini_engine,
    allow_delegation=False
)

extraction_task=Task(
    description="Extract the full transcript from this YouTube URL: {youtube_video_url}",
    expected_output="The raw text transcript of the video.",
    agent=extractor
)

synthesis_task=Task(
    description="Read the Raw Transcript.Summarize it into 3 to 5 highly readable, actionable bullet points.",
    expected_output="A clean markdown summary with a title and bullet points.",
    agent=synthesizer
)

YouTube_crew=Crew(
    agents=[extractor,synthesizer],
    tasks=[extraction_task,synthesis_task],
     verbose=True
)

print("\n========================")
print("🤖 YOUTUBE SUMMARIZER AI BOOT SEQUENCE INITIATED")
print("\n========================\n")

while True:
    target_url=input("Enter Your URL or (Type exit to quit):")

    if target_url.lower()=='exit':
        print("Shutting down agentssss----------")
        break
    
    if "youtube.com" not in target_url  and "youtu.be" not in target_url:
        print("Invalid Link provided as youtube link\n")
        continue
    print("\nDeploying Agents to extract and summarize... Please wait.\n")    
    
    try:
        result=YouTube_crew.kickoff(
             inputs={'youtube_video_url': target_url }
        )
        
        print("\n=========================================")
        print("FINAL ANSWER")
        print(result)
        print("\n=============================\n")

    except Exception as e:
        print(f"\n A system error occurred: {e}\n")

