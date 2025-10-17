
"""
Lab 04: Tools and MCP Integration (Meta Tooling)
Creating self-extending agents that can write and use new tools
"""
import os

from strands import Agent
from strands_tools import editor
from strands.models.anthropic import AnthropicModel

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Get Anthropic API key and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

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
        # With thinking enabled, we need to set the temperature to 1
        "temperature": 1,
        "thinking": {
            "type": "enabled",
            "budget_tokens": 1028
        }
    }
)

# Create self-extending agent with Anthropic Claude 4
agent = Agent(
    model=anthropic_model,
    system_prompt="""
    Goal:
    - Create a python tool under cwd()/tools/*.py using given python tool decorator.
    - I have hot-reloading abilities, after writing the file, I can use it immediately.

    Building tools:

    from strands import tool

    @tool
    def name(name: str, description: str) -> str:
        '''
        Create a tool under cwd()/tools/*.py.
        '''
        return ""
        
    """,
    tools=[editor],
    load_tools_from_directory=True
)

# Example prompts to create and use new tools
prompt = """
Create a tool to add two numbers and then use it to add 5 and 7.
Then create a tool to calculate compound interest and use it to find the value of $1000 at 5% annual interest for 3 years.
"""

# Interactive loop to query the self-extending agent
print("Welcome to the self-extending agent demo!")
print("Type 'exit' or 'quit' to end the session.")
print("Example queries:")
print("- Create a tool to add two numbers")
print("- Create a tool to fetch weather data")
print("- Create a tool to send a message")
print("- Create a tool to calculate compound interest")
while True:

    query = input("\nUser> ").strip()

    if query == "":
        continue

    if query.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break
    
    agent(query)
