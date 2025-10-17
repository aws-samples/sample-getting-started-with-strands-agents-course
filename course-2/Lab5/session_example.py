"""
Lab 5: Simple Session and Conversation Management Demo
A focused demo showing how to implement session management, state tracking,
and conversation management in a Strands agent.
"""
# Import necessary libraries
import os
from pathlib import Path
from dotenv import load_dotenv

from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.session.file_session_manager import FileSessionManager
from strands.agent.conversation_manager import SummarizingConversationManager

# Load environment variables
load_dotenv()


# Get Anthropic API key and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

ANTHROPIC_MODEL_ID = os.getenv("ANTHROPIC_CLAUDE_4", "claude-sonnet-4-20250514")


# Create sessions directory
SESSION_DIR = Path("./sessions")
SESSION_DIR.mkdir(exist_ok=True)
# Create a unique session ID
SESSION_ID = "demo_123"


# Configure Anthropic model
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

# System prompt
SYSTEM_PROMPT = """
You are a helpful assistant that follows the user's instructions carefully.
"""

# Create agent with session and conversation management
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=anthropic_model,
    conversation_manager=conversation_manager,
    session_manager=session_manager,
    state={"user_preferences": {"theme": "dark"}, "session_count": 0}
)

# Get the current state of the agent
agent_state = agent.state.get()
print(f"Initial Agent State: {agent_state}")

# Simulate a user providing personal information
prompt = """
Hi, my name is Alice. I love hiking and reading science fiction novels.
I also enjoy cooking and trying out new recipes.
"""

# Invoke the agent with a prompt
result = agent(prompt)
