"""
Lab 6: Memory Persistent Agents
A focused demo showing how to implement memory management and context awareness in a Strands agent.
"""
# Import necessary libraries
import os

from ddgs import DDGS
from ddgs.exceptions import DDGSException, RatelimitException
from strands import Agent, tool
from strands.models.anthropic import AnthropicModel
from strands_tools import http_request, mem0_memory

from dotenv import load_dotenv

# Load API key from environment
load_dotenv()


# Get Anthropic API key, MEM0 API key, and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
if not ANTHROPIC_API_KEY or not MEM0_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY and MEM0_API_KEY environment variables.")

ANTHROPIC_MODEL_ID = os.getenv("ANTHROPIC_CLAUDE_4", "claude-sonnet-4-20250514")

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
        "temperature": 1,
        "thinking": {
            "type": "enabled",
            "budget_tokens": 1028
        }
    }
)

# Define a mem0 user
USER_ID = "new_mem0_user"

# System prompt for memory agent
SYSTEM_PROMPT = """You are a helpful personal assistant that provides personalized responses based on user history.

Capabilities:
- Store information with mem0_memory (action="store")
- Retrieve memories with mem0_memory (action="retrieve")
- Be sure to include the user_id in all memory tool calls
- Search the web with duckduckgo_search

Key Rules:
- Be conversational and natural
- Retrieve memories before responding
- Store new user information and preferences
- Share only relevant information
- Politely indicate when information is unavailable
"""

@tool
def websearch(keywords: str, region: str = "us-en", max_results: int = 5) -> str:
    """Search the web for updated information.

    Args:
        keywords (str): The search query keywords.
        region (str): The search region: wt-wt, us-en, uk-en, ru-ru, etc..
        max_results (int | None): The maximum number of results to return.
    Returns:
        List of dictionaries with search results.

    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "Rate limit reached. Please try again later."
    except DDGSException as e:
        return f"Search error: {e}"
    

# Initialize agent
memory_agent = Agent(
    model=anthropic_model,
    system_prompt=SYSTEM_PROMPT,
    tools=[mem0_memory, websearch, http_request],
)

# Add first user memory with a direct tool call
memory_agent.tool.mem0_memory(
    action="store", content=f"The user's name is {USER_ID}.", user_id=USER_ID
)

print("=== Memory Agent Session Started ===")
print("Agent's memory was added to message history:")
print(memory_agent.messages)

# List all agent memories
print("=== Agent Memories ===")
# Print all memories for the user
memory_agent.tool.mem0_memory(
                    action="list",
                    user_id=USER_ID,
                )


# Prepare the prompt
prompt = """
Hi are there any articles on building AI Agents with Strands Agents? This is a topic I'm really interested in and would love to learn more about.
"""

# Invoke the agent with a prompt
result = memory_agent(prompt)


# Ask the agent a follow-up question to demonstrate memory retrieval
print("=== === ===" * 5 + "\n")
print("=== === ===")
print("Asking the agent a follow-up question... I want to know more about this Getting Started with Strands Agents")
memory_agent("Ok, I want to know more about this Getting Started with Strands Agents")

# List all agent memories
print("=== === ===" * 5 + "\n")
print("=== Agent Memories ===")
memory_agent("list all of my memories")

