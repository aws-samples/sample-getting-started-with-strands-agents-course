# Import the Agent class from the strands package
from strands import Agent

# Create a specialized agent with a custom system prompt
# Parameters:
#   - model: Specifies which LLM to use (Claude 3.5 Sonnet in this case)
#   - system_prompt: Defines the agent's role, expertise, and response guidelines
dog_breed_helper = Agent(
    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",  # Specifies the Claude 3.5 Sonnet model
    system_prompt="""You are a dog breed expert specializing
    in helping new pet parents decide what breed meets their lifestyles. Your expertise
    covers dog behavior, dog training, basic veterinary care, and dog breed standards.
    
    When giving recommendations:
    1. Provide both benefits and challenges of owning that breed. 
    2. Only provide 3 recommendations at a time.
    3. Give examples when necessary
    4. Avoid jargon, but indicate when complex concepts are important
    
    Your goal is to help pet parents make an informed decision about their choice in a dog.
    """
)

# Define a multi-line query string using triple quotes
# This allows for formatting complex questions with line breaks
query = """
Which dog should I adopt as a first time owner if I have an office job m-f 9-5, like to hike on weekends and don't know much about training?
"""

# Send the query to our specialized dog breed helper agent
# The agent will process the query according to its system prompt instructions
response = dog_breed_helper(query)

# Note: You can create different specialized agents by changing the system prompt
# For example, you could create agents for:
# - Financial advice
# - Cooking instructions
# - Technical support
# - Educational tutoring