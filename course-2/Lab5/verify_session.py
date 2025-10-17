"""
Lab 5: Simple Session and Conversation Management Demo
A focused demo showing how to implement session management, state tracking,
and conversation management in a Strands agent.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.session.file_session_manager import FileSessionManager
from strands.agent.conversation_manager import SummarizingConversationManager


# Load API key from environment
load_dotenv()


# Get Anthropic API key and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

ANTHROPIC_MODEL_ID = os.getenv("ANTHROPIC_CLAUDE_4", "claude-sonnet-4-20250514")


# Note: Requires ANTHROPIC_API_KEY environment variable
anthropic_model = AnthropicModel(
    client_args={
        "api_key": ANTHROPIC_API_KEY
    },
    # **model_config
    # Max tokens is set to 8000
    max_tokens=8000,
    model_id=ANTHROPIC_MODEL_ID,
    params={
        "temperature": 1
    }
)


# Create sessions directory
SESSION_DIR = Path("./sessions")
SESSION_DIR.mkdir(exist_ok=True)
# Create a consistent session ID
SESSION_ID = "demo_123"


# System prompt
SYSTEM_PROMPT = "You are a helpful assistant. Remember information about the user."


# Create session manager
session_manager = FileSessionManager(
    session_id=SESSION_ID,
    storage_dir=str(SESSION_DIR)
)

#Create conversation manager
conversation_manager = SummarizingConversationManager(
    summary_ratio=0.5,              # Summarize 50% of older messages
    preserve_recent_messages=3      # Ensures 3 most recent message pairs (user messages and agent responses) are always kept intact, without summarization
)

# Create agent with session and conversation management
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=anthropic_model,
    conversation_manager=conversation_manager,
    session_manager=session_manager
)



print("=== New Session Started ===")
print("Session ID:", SESSION_ID)
print("Initial session state:", agent.state.get())
print("=== === ===")
print("Asking the agent a question... What is my name and what are my hobbies?")

# Prepare the prompt
prompt = "What is my name and what are my hobbies?"

# Invoke the agent with a prompt
result = agent(prompt)
