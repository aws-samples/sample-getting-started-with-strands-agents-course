# Import the Agent class from the strands package
from strands import Agent

# Import the http_request tool from strands_tools
# This tool allows the agent to make HTTP requests to external websites and APIs
from strands_tools import http_request

# Create a specialized agent with HTTP request capabilities
# Parameters:
#   - model: Specifies which LLM to use (Claude 3.5 Sonnet in this case)
#   - system_prompt: Defines the agent's role, expertise, and response guidelines
#   - tools: List of tools the agent can use (http_request in this case)
dog_breed_helper = Agent(
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",  # Specifies the Claude 3.5 Sonnet model
    system_prompt="""You are a dog breed expert specializing
    in helping new pet parents decide what breed meets their lifestyles. Your expertise
    covers dog behavior, dog training, basic veterinary care, and dog breed standards.
    
    When giving recommendations:
    1. Provide both benefits and challenges of owning that breed. 
    2. Only provide 3 recommendations at a time.
    3. Give examples when necessary
    4. Avoid jargon, but indicate when complex concepts are important
    
    Your goal is to help pet parents make an informed decision about their choice in a dog.
    """,
    tools=[http_request]  # Enables the agent to make HTTP requests to fetch information
)

# Define a multi-line query string that includes a request requiring internet access
# The second question requires the agent to search Wikipedia, which it can do using the http_request tool
query = """
Answer these questions:
1. Which dog should I adopt as a first time owner if I have an office job m-f 9-5, like to hike on weekends and don't know much about training?
2. Search wikipedia for the top 5 most popular dog breeds of the last 5 years.
"""

# Send the query to our agent with HTTP capabilities
# The agent will use its knowledge for question 1 and make an HTTP request for question 2
response = dog_breed_helper(query)

# Note: The http_request tool allows the agent to:
# - Search for information on the web
# - Access APIs (with proper authentication if provided)
# - Retrieve current information that might not be in its training data
# - Verify facts from authoritative sources