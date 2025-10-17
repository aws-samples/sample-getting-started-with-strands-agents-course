"""
Lab 01: Overview of Strands Agents
A simple introduction to creating and using agents with the Strands SDK
"""
# Import the Strands Agent
from strands import Agent
from pprint import pprint


# ============================================================
# Example 1: Building Your First Agent
# ============================================================
print("Example 1: Building Your First Agent")
# Create the simplest agent - just 1 line!
agent = Agent()

# Send a message to the agent
result = agent("What is Agentic AI? Explain in 2 sentences.")


# Print the agent result
print("\n")
print("-" * 100)
print("\n")
print(f"Agent result:\n{result}\n")
print("-" * 100)
print("\n")

# AgentResult object contains:
# Print the last generated agent message
print(f"Last generated agent message: {result.message}")
print("-" * 100)
print("\n")

# Prints the metrics
pprint(f"Metrics: {result.metrics}")
print("-" * 100)
print("\n")

# Prints the state
print(f"State: {result.state}")
print("-" * 100)
print("\n")

# Prints the stop reason
print(f"Stop Reason: {result.stop_reason}")
print("-" * 100)
print("\n")

# ============================================================
# Example 2: Understanding the Agent Interface
# ============================================================
print("Example 2: Understanding the Agent Interface")
# Check the current model being used by the agent
print(f"Current Agent model provider: {agent.model}")
print(f"Current Agent model id: {agent.model.config['model_id']}")
print("-" * 100)
print("\n")

# Update the agent model to use Claude 3.5
agent.model.config['model_id'] = "us.anthropic.claude-3-5-haiku-20241022-v1:0"

print(f"Updated Agent model: {agent.model.config['model_id']}")
print("-" * 100)
print("\n")

# Check current system prompt
print(f"Current Agent system prompt: {agent.system_prompt}")
print("-" * 100)
print("\n")

# Update the system prompt
agent.system_prompt = "You are a helpful assistant."

print(f"Updated Agent system prompt: {agent.system_prompt}")
print("-" * 100)
print("\n")

# Check Agent messages loaded into the conversation
print(f"Current Agent messages: {agent.messages}")
print(f"Number of messages in the conversation: {len(agent.messages)}")
print("-" * 100)
print("\n")

# Add a message to the conversation
agent("What comes after 2 in the Fibonacci sequence?")

# Check the number of messages in the conversation again
print(f"Updated current Agent messages: {agent.messages}")
print(f"Number of messages in the conversation: {len(agent.messages)}")
print("-" * 100)
print("\n")

# Remove all messages
print("Clearing all messages...")
agent.messages.clear()

print(f"Cleared Agent messages: {agent.messages}")
print("-" * 100)
print("\n")
