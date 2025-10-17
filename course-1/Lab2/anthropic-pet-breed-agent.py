# Import necessary libraries
import os                                     # For accessing environment variables
from strands import Agent                    # Import the Agent class from strands library
from strands.models.anthropic import AnthropicModel  # Import Anthropic's language model
from strands_tools import http_request       # Import tool for making HTTP requests
from dotenv import load_dotenv               # For loading environment variables from .env file

load_dotenv()

# Configure the Anthropic language model (Claude)
model = AnthropicModel(
    # Set up authentication using API key from environment variables
    client_args={
        "api_key": os.getenv("api_key"),  # Get API key from environment variables
    },
    # **model_config
    max_tokens=1028,                    # Set maximum response length to 1028 tokens
    model_id="claude-sonnet-4-20250514",  # Specify which Claude model version to use
    params={
        "temperature": 0.3,              # Set temperature to 0.3 (lower values make output more deterministic)
    }
)

# Create an AI agent specialized in dog breed recommendations
dog_breed_helper = Agent(
    model=model,                      # Use the Anthropic model configured above
              
    # Define the agent's personality and expertise through a system prompt
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
              
    # Give the agent access to the http_request tool so it can search the web
    tools=[http_request]
)

# Define a multi-part query for the dog breed agent
# First question requires the agent to use its knowledge base
# Second question requires the agent to search the web using the http_request tool
query = """
Answer these questions:
1. Which dog should I adopt as a first time owner if I have an office job m-f 9-5, like to hike on weekends and don't know much about training?
2. Search wikipedia for the top 5 most popular dog breeds of the last 5 years.
"""

# Send the query to the agent with HTTP capabilities
# The agent will use its knowledge for question 1 and make an HTTP request for question 2
response = dog_breed_helper(query)