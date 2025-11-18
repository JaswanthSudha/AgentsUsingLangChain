from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import tools
from langchain.chat_models import init_chat_model


load_dotenv()


class EmailResponse(BaseModel):
    """Structured response for email generation"""

    recipient: str = Field(description="The recipient's name or email address")
    subject: str = Field(description="The email subject line")
    email_body: str = Field(description="The complete email body content")
    tone: str = Field(
        description="The tone used in the email (formal, casual, friendly, professional)"
    )
    tools_used: list[str] = Field(
        description="List of tools used to generate the email"
    )
    recommendations: str = Field(description="Recommendations for improving the email")


# Initialize the language model
# You can use different models: "openai:gpt-4", "anthropic:claude-3-5-sonnet-20241022", "googl    email_response = extract_email_response(result)e_genai:gemini-2.5-flash-lite"
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# Create agent with modern LangChain appuggesting improvements for clarity and professionalroach
system_prompt = """
You are an expert email writing assistant that helps users compose professional, clear, and effective emails.

Your responsibilities include:
- Understanding the user's email requirements (purpose, recipient, tone)
- Drafting appropriate emails based on the context
- Suggesting improvements for clarity and professionalism
- Using templates when appropriate
- Ensuring proper email structure and formatting
- Adapting tone based on the situation (formal, casual, friendly, professional)
- Validating email addresses before sending
- Actually sending emails when the user provides a recipient email address and requests to send

When generating emails, always:
1. Identify the recipient and purpose
2. Choose an appropriate subject line
3. Craft a well-structured body with clear opening, middle, and closing
4. Match the requested tone
5. Use proper email etiquette
6. Provide recommendations for improvement if needed
7. If user wants to send the email, validate the email address first, then use the send_email tool

Available tools you can use:    email_response = extract_email_response(result)
- draft_email: Draft an email with given details
- save_email_draft: Save the draft to a file
- generate_email_template: Generate templates for common email types
- format_email_signature: Create professional email signatures
- check_email_length: Analyze email length
- send_email: Send the email to a recipient (validate email first)
- validate_email_address: Check if email address is valid

IMPORTANT: After using tools and gathering information, you MUST provide your final response in the following structured format:

recipient: [recipient name or email]
subject: [email subject line]
email_body: [complete email body with proper formatting]
tone: [formal/casual/friendly/professional]
tools_used: [list of tools you used, e.g., "draft_email, validate_email_address"]
recommendations: [any suggestions for improving the email]    email_response = extract_email_response(result)

Be helpful, professional, and thorough in your email composition.
"""

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ToolStrategy(EmailResponse),
)

# Main interaction loop
print("\n" + "=" * 50)
print("    EMAIL GENERATION AGENT")
print("=" * 50)
print("\nWelcome! I can help you generate professional emails.")
print("Examples:")
print("- 'Write a follow-up email to John about the project deadline'")
print("- 'Draft a thank you email to my mentor'")
print("- 'Create a formal request email for time off'")
print("\nType 'quit' or 'exit' to stop.\n")

while True:
    query = input("\n📧 What email would you like to generate? ")

    if query.lower() in ["quit", "exit", "q"]:
        print("\nThank you for using Email Generation Agent! Goodbye! 👋\n")
        break

    if not query.strip():
        print("Please provide details about the email you want to generate.")
        continue
    try:
        print("\n🤖 Generating your email...\n")
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})

    except Exception as e:
        print(f"\n❌ Error generating email: {str(e)}")
        print("Please try again with a different request.\n")
