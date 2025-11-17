from dotenv import load_dotenv

load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-Nemo-Instruct-2407",  # Any free text-generating model
    task="text-generation",
)

response = llm.generate(["Write a poem about AI assisting humans:"])
print(response)
