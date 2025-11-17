from dotenv import load_dotenv
from pydantic import BaseModel
import os 
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import tools
from langchain.chat_models import init_chat_model


load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))


model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# Create agent with modern LangChain approach
system_prompt = """
You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools.
Provide your response in a structured format with:
- A clear topic identification
- A comprehensive summary of your findings
- List of sources you referenced
- List of tools you used during research

Be thorough and accurate in your research.
"""

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ToolStrategy(ResearchResponse)
)

query = input("Enter your research topic: ")
result = agent.invoke({"messages": [{"role": "user", "content": query}]})