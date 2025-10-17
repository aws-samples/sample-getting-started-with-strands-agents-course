# Import necessary libraries
import os                                     # For accessing environment variables
from strands import Agent                    # Import the Agent class from strands library
from strands.models.anthropic import AnthropicModel  # Import Anthropic's language model
from strands_tools import generate_image,current_time # Import image generator and current time tools
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
    model_id="claude-3-7-sonnet-20250219",  # Specify which Claude model version to use
    params={
        "temperature": 0.3,              # Set temperature to 0.3 (lower values make output more deterministic)
    }
)

# Create a general-purpose AI agent with AWS capabilities
agent = Agent(
    model=model,                      # Use the Anthropic model configured above
    tools=[generate_image,current_time]       # Give the agent access to the image generator and current time tools
)

# Define a query 
query = "Generate an image of a husky surfing on a surfboard in the Philippines. Also share the current time after you generate the image"

# Send the query to the agent and store the response
response = agent(query)