"""
Lab 03: Implementing Advanced Hooks for Tool Argument Manipulation
Demonstrates how to create and register custom hooks to manipulate tool arguments before invocation
"""
import os
from typing import Any

from strands import Agent
from strands_tools import calculator
from strands.models.anthropic import AnthropicModel
from strands.hooks import HookProvider, HookRegistry
from strands.experimental.hooks import BeforeToolInvocationEvent

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get Anthropic API key and model ID from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

ANTHROPIC_MODEL_ID = os.getenv("ANTHROPIC_CLAUDE_4", "claude-sonnet-4-20250514")


class ConstantToolArguments(HookProvider):
    """Use constant argument values for specific parameters of a tool."""

    def __init__(self, fixed_tool_arguments: dict[str, dict[str, Any]]):
        """
        Initialize fixed parameter values for tools.

        Args:
            fixed_tool_arguments: A dictionary mapping tool names to dictionaries of 
                parameter names and their fixed values. These values will override any 
                values provided by the agent when the tool is invoked.
        """
        self._tools_to_fix = fixed_tool_arguments

    def register_hooks(self, registry: HookRegistry, **kwargs: Any) -> None:
        print("Registering ConstantToolArguments hook")
        registry.add_callback(BeforeToolInvocationEvent, self._fix_tool_arguments)

    def _fix_tool_arguments(self, event: BeforeToolInvocationEvent):
        # If the tool is in our list of parameters, then use those parameters
        if parameters_to_fix := self._tools_to_fix.get(event.tool_use["name"]):
            tool_input: dict[str, Any] = event.tool_use["input"]
            tool_input.update(parameters_to_fix)


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
        "temperature": 0,
    }
)


# Define fixed parameters for the calculator tool
fix_parameters = ConstantToolArguments({
    "calculator": {
        "precision": 1,
    }
})


# Create agent with Anthropic Claude 4
agent = Agent(
    model=anthropic_model,
    tools=[calculator], 
    hooks=[fix_parameters]
)

# Invoke the agent with a query that uses the calculator tool
agent("What is 2 / 3?")
