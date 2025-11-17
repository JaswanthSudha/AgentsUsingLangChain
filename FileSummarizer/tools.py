from langchain.tools import tool
from datetime import datetime
from typing import Optional


@tool
def save_to_txt(data: str, filename: Optional[str] = "summanry_output.txt") -> str:
    """
    Save summary data to a text file with timestamp.
    
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

    save_to_txt
]