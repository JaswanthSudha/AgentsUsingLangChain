from langchain.tools import tool
from datetime import datetime
from typing import Optional, Literal
import os

@tool
def draft_email(
    recipient: str,
    subject: str,
    body: str,
    tone: Literal["formal", "casual", "friendly", "professional"] = "professional"
) -> str:
    """
    Draft an email with the given details.
    
    Args:
        recipient: The name or email address of the recipient
        subject: The subject line of the email
        body: The main content/body of the email
        tone: The tone of the email (formal, casual, friendly, professional)
        
    Returns:
        Formatted email draft
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        email_draft = f"""
========================================
EMAIL DRAFT
========================================
To: {recipient}
Subject: {subject}
Tone: {tone.capitalize()}
Draft Created: {timestamp}
----------------------------------------

{body}

----------------------------------------
"""
        return email_draft
    except Exception as e:
        return f"Failed to draft email: {str(e)}"


@tool
def save_email_draft(email_content: str, filename: Optional[str] = None) -> str:
    """
    Save email draft to a text file.
    
    Args:
        email_content: The complete email content to save
        filename: Optional filename (if not provided, auto-generates with timestamp)
        
    Returns:
        Confirmation message about the saved file
    """
    try:
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"email_draft_{timestamp}.txt"
        
        # Create drafts directory if it doesn't exist
        drafts_dir = "email_drafts"
        os.makedirs(drafts_dir, exist_ok=True)
        
        filepath = os.path.join(drafts_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(email_content)
        
        return f"Email draft successfully saved to {filepath}"
    except Exception as e:
        return f"Failed to save email draft: {str(e)}"


@tool
def generate_email_template(
    template_type: Literal[
        "introduction",
        "follow_up",
        "thank_you",
        "apology",
        "invitation",
        "announcement",
        "request",
        "confirmation"
    ],
    context: str
) -> str:
    """
    Generate an email template based on the type and context provided.
    
    Args:
        template_type: The type of email template to generate
        context: Specific context or details to include in the template
        
    Returns:
        Email template with placeholders and structure
    """
    templates = {
        "introduction": """
Subject: Introduction - [Your Purpose]

Dear [Recipient Name],

I hope this email finds you well. My name is [Your Name] and I am reaching out to introduce myself.

{context}

I would appreciate the opportunity to connect and discuss this further.

Best regards,
[Your Name]
""",
        "follow_up": """
Subject: Following Up - [Original Topic]

Dear [Recipient Name],

I wanted to follow up on [previous conversation/email/meeting].

{context}

Please let me know if you need any additional information.

Best regards,
[Your Name]
""",
        "thank_you": """
Subject: Thank You - [Reason]

Dear [Recipient Name],

I wanted to take a moment to thank you for [specific action/help].

{context}

Your support is greatly appreciated.

Warm regards,
[Your Name]
""",
        "apology": """
Subject: Apology - [Situation]

Dear [Recipient Name],

I am writing to apologize for [situation].

{context}

I appreciate your understanding and patience.

Sincerely,
[Your Name]
""",
        "invitation": """
Subject: Invitation - [Event Name]

Dear [Recipient Name],

You are cordially invited to [event/meeting/occasion].

{context}

Please let me know if you can attend.

Best regards,
[Your Name]
""",
        "announcement": """
Subject: Announcement - [Topic]

Dear [Recipient Name],

I am pleased to announce [announcement].

{context}

Please feel free to reach out if you have any questions.

Best regards,
[Your Name]
""",
        "request": """
Subject: Request - [What You Need]

Dear [Recipient Name],

I am writing to request [specific request].

{context}

I would greatly appreciate your assistance with this matter.

Thank you for your consideration.

Best regards,
[Your Name]
""",
        "confirmation": """
Subject: Confirmation - [What is Being Confirmed]

Dear [Recipient Name],

This email is to confirm [details being confirmed].

{context}

Please let me know if any changes are needed.

Best regards,
[Your Name]
"""
    }
    
    template = templates.get(template_type, "")
    return template.replace("{context}", context)


@tool
def format_email_signature(
    name: str,
    title: Optional[str] = None,
    company: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    website: Optional[str] = None
) -> str:
    """
    Generate a professional email signature.
    
    Args:
        name: Full name
        title: Job title
        company: Company name
        phone: Phone number
        email: Email address
        website: Website URL
        
    Returns:
        Formatted email signature
    """
    signature_parts = [f"\n{name}"]
    
    if title:
        signature_parts.append(title)
    if company:
        signature_parts.append(company)
    if phone:
        signature_parts.append(f"Phone: {phone}")
    if email:
        signature_parts.append(f"Email: {email}")
    if website:
        signature_parts.append(f"Website: {website}")
    
    signature = "\n".join(signature_parts)
    return f"""
----------------------------------------
{signature}
----------------------------------------
"""


@tool
def check_email_length(email_body: str) -> str:
    """
    Analyze email length and provide recommendations.
    
    Args:
        email_body: The email body text to analyze
        
    Returns:
        Analysis of email length with recommendations
    """
    word_count = len(email_body.split())
    char_count = len(email_body)
    
    if word_count < 50:
        recommendation = "Email is concise. Good for quick messages."
    elif word_count < 150:
        recommendation = "Email length is optimal for professional communication."
    elif word_count < 300:
        recommendation = "Email is somewhat long. Consider breaking into sections."
    else:
        recommendation = "Email is very long. Consider summarizing or using attachments."
    
    return f"""
Email Length Analysis:
- Word Count: {word_count}
- Character Count: {char_count}
- Recommendation: {recommendation}
"""


# List of all tools available to the email agent
tools = [
    draft_email,
    save_email_draft,
    generate_email_template,
    format_email_signature,
    check_email_length
]
