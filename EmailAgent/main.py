from dotenv import load_dotenv
from pydantic import BaseModel
import os 
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import tools
from langchain.chat_models import init_chat_model


load_dotenv()

class EmailResponse(BaseModel):
    """Structured response for email generation"""
    recipient: str
    subject: str
    email_body: str
    tone: str
    tools_used: list[str]
    recommendations: str

# Initialize the language model
# You can use different models: "openai:gpt-4", "anthropic:claude-3-5-sonnet-20241022", "google_genai:gemini-2.5-flash-lite"
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# Create agent with modern LangChain approach
system_prompt = """
You are an expert email writing assistant that helps users compose professional, clear, and effective emails.

Your responsibilities include:
- Understanding the user's email requirements (purpose, recipient, tone)
- Drafting appropriate emails based on the context
- Suggesting improvements for clarity and professionalism
- Using templates when appropriate
- Ensuring proper email structure and formatting
- Adapting tone based on the situation (formal, casual, friendly, professional)

When generating emails, always:
1. Identify the recipient and purpose
2. Choose an appropriate subject line
3. Craft a well-structured body with clear opening, middle, and closing
4. Match the requested tone
5. Use proper email etiquette
6. Provide recommendations for improvement if needed

Provide your response in a structured format with:
- Recipient name/email
- Subject line
- Complete email body
- Tone used
- List of tools you utilized
- Any recommendations for the email

Be helpful, professional, and thorough in your email composition.
"""

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ToolStrategy(EmailResponse)
)

# Main interaction loop
print("\n" + "="*50)
print("    EMAIL GENERATION AGENT")
print("="*50)
print("\nWelcome! I can help you generate professional emails.")
print("Examples:")
print("- 'Write a follow-up email to John about the project deadline'")
print("- 'Draft a thank you email to my mentor'")
print("- 'Create a formal request email for time off'")
print("\nType 'quit' or 'exit' to stop.\n")

while True:
    query = input("\n📧 What email would you like to generate? ")
    
    if query.lower() in ['quit', 'exit', 'q']:
        print("\nThank you for using Email Generation Agent! Goodbye! 👋\n")
        break
    
    if not query.strip():
        print("Please provide details about the email you want to generate.")
        continue
    
    try:
        print("\n🤖 Generating your email...\n")
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})
        
        # Extract the structured response
        if hasattr(result, 'structured_response'):
            email_data = result.structured_response
            
            # Display the generated email in clean format
            print("\n" + "="*70)
            print("                         GENERATED EMAIL")
            print("="*70)
            print(f"\n📨 TO:      {email_data.recipient}")
            print(f"📋 SUBJECT: {email_data.subject}")
            print(f"🎨 TONE:    {email_data.tone.capitalize()}")
            print("\n" + "-"*70)
            print("EMAIL BODY:")
            print("-"*70)
            print(f"\n{email_data.email_body}\n")
            print("-"*70)
            print("\n🔧 TOOLS USED:")
            for tool in email_data.tools_used:
                tool_name = tool.replace("default_api.", "")
                print(f"   ✓ {tool_name}")
            print("\n💡 RECOMMENDATIONS:")
            print(f"   {email_data.recommendations}")
            print("\n" + "="*70)
        else:
            print("\n" + "="*50)
            print("GENERATED EMAIL")
            print("="*50)
            print(result)
            
    except Exception as e:
        print(f"\n❌ Error generating email: {str(e)}")
        print("Please try again with a different request.\n")