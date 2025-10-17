"""
Lab 03: Implementing Basic Hooks for Logging 
Demonstrates how to create and register custom hooks for logging agent events
"""
import os

from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.hooks import HookProvider, HookRegistry
from strands.hooks import BeforeInvocationEvent, AfterInvocationEvent

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Get Anthropic API key and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

ANTHROPIC_MODEL_ID = os.getenv("ANTHROPIC_CLAUDE_4", "claude-sonnet-4-20250514")

# Register custom hooks for logging
class LoggingHook(HookProvider):
    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeInvocationEvent, self.log_start)
        registry.add_callback(AfterInvocationEvent, self.log_end)

    # Log the start of the request
    def log_start(self, event: BeforeInvocationEvent) -> None:
        print("\n")
        print(f"Request started for agent: {event.agent.name}")
        print("\n")
        print("-" * 100)
        print("\n")

    # Log the end of the request
    def log_end(self, event: AfterInvocationEvent) -> None:
        print("\n")
        print("-" * 100)
        print(f"\nRequest completed for agent: {event.agent.name}")
        print("\n")


# Configure Anthropic model
# Note: Requires ANTHROPIC_API_KEY environment variable
anthropic_model = AnthropicModel(
    client_args={
        "api_key": ANTHROPIC_API_KEY
    },
    # **model_config
    # Max tokens is set to 1000
    max_tokens=1000,
    model_id=ANTHROPIC_MODEL_ID,
    params={
        # With thinking enabled, we need to set the temperature to 1
        "temperature": 1,
    }
)

# Create agent with Anthropic Claude 4
agent = Agent(
    model=anthropic_model,
    hooks=[LoggingHook()]
    )

# Invoke Agent
agent("Tell me a 1 line joke about computers.")
