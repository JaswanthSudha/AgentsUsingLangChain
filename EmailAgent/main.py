from langchain.agents import create_agent
from dotenv import load_dotenv
import os 
load_dotenv()
# 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
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

model = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

chat = ChatHuggingFace(llm=model, verbose=True)
messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
try:
    chat.invoke(messages)
except Exception as e:
    print(f"Error during chat invocation: {e}")
    