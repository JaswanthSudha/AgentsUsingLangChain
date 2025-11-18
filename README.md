# 🤖 AI Agents Using LangChain

A collection of intelligent AI agents built with LangChain that can perform various tasks including email generation, file summarization, and research assistance.

## 📋 Table of Contents

- [Overview](#overview)
- [Agents](#agents)
  - [Email Agent](#email-agent)
  - [File Summarizer](#file-summarizer)
  - [Research Agent](#research-agent)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project demonstrates the power of LangChain in creating autonomous AI agents that can use tools, make decisions, and complete complex tasks. Each agent is specialized for specific use cases and equipped with relevant tools to accomplish its objectives.

## 🤖 Agents

### 📧 Email Agent

An intelligent email writing assistant that helps you compose professional, clear, and effective emails.

**Capabilities:**

- Draft emails with customizable tone (formal, casual, friendly, professional)
- Generate email templates for common scenarios
- Validate email addresses
- Send emails directly via SMTP
- Save email drafts to files
- Format professional email signatures
- Check email length and provide recommendations
- Suggest improvements for clarity and professionalism

**Tools Available:**

- `draft_email` - Create structured emails
- `generate_email_template` - Generate templates (introduction, follow-up, thank you, etc.)
- `validate_email_address` - Validate email format
- `send_email` - Send emails via SMTP
- `save_email_draft` - Save drafts to text files
- `format_email_signature` - Create professional signatures
- `check_email_length` - Analyze email length

**Example Prompts:**

```
- "Write a follow-up email to John about the project deadline"
- "Draft a thank you email to my mentor"
- "Create a formal request email for time off"
- "Send an email to john@example.com thanking him for the meeting"
```

### 📄 File Summarizer

An agent designed to analyze and summarize documents and files efficiently.

### 🔍 Research Agent

An intelligent research assistant that can gather, analyze, and synthesize information from various sources.

## ✨ Features

- **Multi-Agent Architecture**: Specialized agents for different tasks
- **Tool Integration**: Each agent has access to relevant tools
- **Structured Output**: Uses Pydantic models for consistent responses
- **Multiple LLM Support**: Compatible with OpenAI, Anthropic, Google, and Hugging Face models
- **Interactive CLI**: User-friendly command-line interface
- **Environment Configuration**: Secure credential management via `.env` files
- **Email Functionality**: Full SMTP integration for sending emails

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JaswanthSudha/AgentsUsingLangChain.git
   cd AgentsUsingLangChain
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv310
   source venv310/bin/activate  # On Windows: venv310\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create a `.env` file** in the project root by copying the example:

   ```bash
   cp env.example .env
   ```

2. **Add your API keys and configurations** to `.env`:

   ```env
   # LLM API Keys (add the ones you plan to use)
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here

   # Email Configuration (for Email Agent)
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_app_password_here
   ```

3. **For Gmail users:**
   - Enable 2-Factor Authentication on your Google account
   - Generate an [App Password](https://support.google.com/accounts/answer/185833)
   - Use the App Password (not your regular password) in `SENDER_PASSWORD`

## 🎮 Usage

### Running the Email Agent

```bash
cd EmailAgent
python main.py
```

**Interactive Example:**

```
================================================
    EMAIL GENERATION AGENT
================================================

Welcome! I can help you generate professional emails.
Examples:
- 'Write a follow-up email to John about the project deadline'
- 'Draft a thank you email to my mentor'
- 'Create a formal request email for time off'

Type 'quit' or 'exit' to stop.

📧 What email would you like to generate? Write a professional email to sarah@company.com thanking her for the interview

🤖 Generating your email...

========================================
       GENERATED EMAIL DETAILS
========================================
To: sarah@company.com
Subject: Thank You for the Interview Opportunity
Tone: Professional
----------------------------------------
Dear Sarah,

I wanted to take a moment to express my sincere gratitude...
----------------------------------------
Tools Used: draft_email, validate_email_address
💡 Recommendations: Consider adding specific details about...
========================================
```

### Running Other Agents

```bash
# File Summarizer
cd FileSummarizer
python main.py

# Research Agent
cd ResearchAgent
python main.py
```

## 📁 Project Structure

```
Agent/
├── EmailAgent/
│   ├── __init__.py
│   ├── main.py          # Email agent entry point
│   ├── tools.py         # Email-specific tools
│   └── __pycache__/
├── FileSummarizer/
│   ├── main.py          # File summarizer entry point
│   └── tools.py         # Summarization tools
├── ResearchAgent/
│   ├── __init__.py
│   ├── main.py          # Research agent entry point
│   └── tools.py         # Research tools
├── venv310/             # Virtual environment
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables template
└── README.md           # This file
```

## 🛠️ Technologies Used

- **LangChain**: Framework for building LLM applications
- **LangGraph**: For agent orchestration and workflows
- **Pydantic**: Data validation and structured outputs
- **Python-dotenv**: Environment variable management
- **DuckDuckGo Search**: Web search capabilities
- **SMTP**: Email sending functionality
- **Supported LLMs**:
  - OpenAI (GPT-4, GPT-3.5)
  - Anthropic (Claude)
  - Google (Gemini)
  - Hugging Face Models

## 🎯 Model Selection

The agents support multiple LLM providers. You can switch models by modifying the `init_chat_model()` call:

```python
# OpenAI
model = init_chat_model("openai:gpt-4")

# Anthropic
model = init_chat_model("anthropic:claude-3-5-sonnet-20241022")

# Google
model = init_chat_model("google_genai:gemini-2.5-flash-lite")
```

## 📝 Email Agent - Detailed Features

### Supported Email Templates

The Email Agent can generate templates for:

- **Introduction**: First-time contact emails
- **Follow-up**: Check-in and reminder emails
- **Thank You**: Gratitude and appreciation
- **Apology**: Professional apologies
- **Invitation**: Event and meeting invitations
- **Announcement**: Company or team announcements
- **Request**: Formal requests
- **Confirmation**: Acknowledgment emails

### Email Tones

Choose from different tones to match your communication style:

- **Formal**: Business and official communications
- **Professional**: Standard workplace communication
- **Friendly**: Warm but professional
- **Casual**: Relaxed and informal

## 🔒 Security Best Practices

- Never commit your `.env` file to version control
- Use App Passwords instead of regular passwords for email
- Rotate API keys regularly
- Keep dependencies updated
- Review generated emails before sending

## 🐛 Troubleshooting

### Email Sending Issues

**Problem**: Authentication failed

- **Solution**: Ensure you're using an App Password for Gmail, not your regular password

**Problem**: Connection refused

- **Solution**: Check SMTP server and port settings. For Gmail, use `smtp.gmail.com:587`

### LLM API Issues

**Problem**: API key invalid

- **Solution**: Verify your API key in `.env` file is correct and active

**Problem**: Rate limit exceeded

- **Solution**: Wait a few minutes or upgrade your API plan

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

- **Jaswanth Sudha** - [GitHub](https://github.com/JaswanthSudha)

## 🙏 Acknowledgments

- LangChain team for the excellent framework
- OpenAI, Anthropic, and Google for their powerful LLMs
- The open-source community

## 📞 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

---

**Made with ❤️ using LangChain**
