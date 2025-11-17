from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime
from typing import Optional

# Initialize the search and wikipedia utilities
_search = DuckDuckGoSearchRun()
_wikipedia = WikipediaAPIWrapper()

@tool
def duckduckgo_search(query: str) -> str:
    """
    Search for information using DuckDuckGo.
    
    Args:
        query: The search query to look up current events or specific information online
        
    Returns:
        Search results from DuckDuckGo
    """
    try:
        return _search.run(query)
    except Exception as e:
        return f"Search failed: {str(e)}"

@tool 
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia for information about people, places, concepts, or things.
    
    Args:
        query: The topic to search for on Wikipedia
        
    Returns:
        Wikipedia article content or summary
    """
    try:
        return _wikipedia.run(query)
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}"

@tool
def save_to_txt(data: str, filename: Optional[str] = "research_output.txt") -> str:
    """
    Save research data to a text file with timestamp.
    
    Args:
        data: The text content to save to the file
        filename: Optional filename (defaults to "research_output.txt")
        
    Returns:
        Confirmation message about the saved file
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_text)
        
        return f"Data successfully saved to {filename}"
    except Exception as e:
        return f"Failed to save file: {str(e)}"

# List of all tools available to the agent
tools = [
    duckduckgo_search,
    wikipedia_search, 
    save_to_txt
]