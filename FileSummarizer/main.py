from dotenv import load_dotenv
from pydantic import BaseModel
import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.agents.structured_output import ToolStrategy
load_dotenv()
from tools import tools

class FileSummaryResponse(BaseModel):
    filename: str
    summary: str
    key_points: list[str]
    tools_used: list[str]
model=init_chat_model("google_genai:gemini-2.5-flash-lite")
system_prompt="""
You are a file summarization assistant.
Given a file, provide a concise summary and highlight key points.
Provide your response in a structured format with:
- The filename
- A concise summary of the file content
- A list of key points from the file
- A list of tools you used during summarization
Be thorough and accurate in your summarization. and save the summary into a text file using the provided"""
agent=create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ToolStrategy(FileSummaryResponse)
)
file_path=input("Enter the path to the file to summarize: ")
with open(file_path, 'r') as file:
    file_content=file.read()
result=agent.invoke({"messages":[{"role":"user","content":file_content}]})
print(result)