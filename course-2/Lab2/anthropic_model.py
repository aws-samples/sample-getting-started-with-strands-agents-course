"""
Lab 02: Model Providers and Configuration
Configuring agents with different LLM providers
"""
# ============================================================
# Anthropic Model
# ============================================================
import os

from strands import Agent
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
    # Max tokens is set to 4096 to allow for extended thinking tokens
    max_tokens=4096,
    model_id=ANTHROPIC_MODEL_ID,
    params={
        # With thinking enabled, we need to set the temperature to 1
        "temperature": 1,
        # Adding extended thinking tokens
        "thinking": {
            "type": "enabled",
            "budget_tokens": 1028
        }
    }
)

# Create agent with Anthropic Claude 4
agent = Agent(model=anthropic_model)



# Invoke the agent with a prompt
result = agent("Give me the best word to describe generative AI?")

# print the result message
print("\n")
print("-" * 100)
print("\n")
print(f"Result: {result}")
print("-" * 100)
print("\n")

# Prints the metrics
print(f"Metrics: {result.metrics}")
print("-" * 100)
print("\n")
