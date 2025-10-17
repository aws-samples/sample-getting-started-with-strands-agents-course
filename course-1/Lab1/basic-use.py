# Import the Agent class from the strands package
# The Agent class provides AI capabilities for question answering and other tasks
from strands import Agent

# Create a new agent instance with default settings
# This initializes the agent with standard configuration parameters
# You can customize the agent by passing parameters to the Agent constructor
agent = Agent()

# Ask the agent a question by calling the agent instance like a function
# The agent will process the question and return a response
response = agent("What is Agentic AI?")

# Note: You can ask different types of questions by changing the string passed to the agent
# For example: agent("What is the capital of France?")
# or agent("Explain how photosynthesis works")