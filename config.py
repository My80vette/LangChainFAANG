import anthropic
import langchain
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Claude API client
claude_api_key = os.getenv('ANTHROPIC_API_KEY')
if not claude_api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

# Initialize Claude client
claude_client = anthropic.Anthropic(api_key=claude_api_key)

# Initialize LangChain's ChatAnthropic instance
claude_llm = ChatAnthropic(
    model="claude-3-7-sonnet-20250219",
    anthropic_api_key=claude_api_key,
    max_tokens=1024
)
