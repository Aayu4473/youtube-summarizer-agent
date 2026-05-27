from langchain_community.document_loaders import YoutubeLoader
from crewai_tools import tool

#decorative tool
@tool("Youtube Transcript Extractor")
def extract_youtube_transcript(youtube_url: str) -> str:
    """Use this tool to extract the raw text transcript from a youtube video url."""
    try:
        loader=YoutubeLoader.from_youtube_url(youtube_url,add_video_info=False)
        docs=loader.load() #langchain reaches out to the internet and download caption file and store in docs tell langchain to download the data 
        #extract just the raw text and hand it to the agent
        if docs:
            return docs[0].page_content
        else:
            return "Error: no transcript found"
    except Exception as e:
        return f"Error extracting transcript: {str(e)}"
    

